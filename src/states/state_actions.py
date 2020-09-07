import json
import abc
from collections import namedtuple
from datetime import date, datetime
from dateutil import relativedelta

from src.actions_executors.iexecutors import IDdoser, IHtmlExtractor, ITelegramBot, ICaptchaSolver, PersonInfo
from src.states.istate_actions import IStateActions, ActionError


class IPersonInfoGetter(abc.ABC):
    @abc.abstractmethod
    def get_person_info(self) -> PersonInfo:
        pass


class PersonInfoGetter(IPersonInfoGetter):
    def get_person_info(self) -> PersonInfo:
        return self._read_person_info()

    @staticmethod
    def _read_person_info() -> PersonInfo:
        with open('data.json', 'r', encoding='utf-8') as f:
            data = json.load(f)
            return PersonInfoGetter._convert(data)

    @staticmethod
    def _convert(dictionary):
        return namedtuple('PersonInfo', dictionary.keys())(**dictionary)


def format_date(formatting_date: date) -> str:
    return f'{formatting_date.day}.{formatting_date.month}.{formatting_date.year}'


def format_today() -> str:
    return format_date(date.today())


def format_next_month() -> str:
    return format_date(date.today() + relativedelta.relativedelta(months=1))


class StateActions(IStateActions):
    def __init__(self, ddoser: IDdoser, extractor: IHtmlExtractor, bot: ITelegramBot, solver: ICaptchaSolver,
                 info_getter: IPersonInfoGetter):
        self._ddoser = ddoser
        self._extractor = extractor
        self._bot = bot
        self._solver = solver
        self._info_getter = info_getter
        self._day_href = ''

    async def get_current_month_and_solve_captcha(self):
        await self._captcha_solved(await self._ddoser.get_month(format_today()))

    async def check_free_places_in_current_month(self) -> str:
        self._day_href = await self._check_free_places(format_today())
        return self._day_href

    async def check_free_places_in_next_month(self) -> str:
        self._day_href = await self._check_free_places(format_next_month())
        return self._day_href

    async def try_to_reserve_place(self, detected_day_href: str = '') -> bool:
        if not detected_day_href:
            detected_day_href = self._day_href

        print(datetime.now(), ' Found day slot, trying to reserve place!')
        await self._bot.notify_subscribers('Found day slot, trying to reserve place! -> ' + detected_day_href)

        day_in_response = await self._ddoser.get_day(detected_day_href)
        time_href = self._extractor.extract_time_href(day_in_response)
        print('Time ->', time_href)

        if not time_href:
            return False

        time_form_in_response = await self._ddoser.get_time_slot(time_href)
        hidden_fields = self._extractor.extract_hidden_fields(time_form_in_response)
        print(hidden_fields)

        if not hidden_fields:
            return False

        captcha = self._extractor.extract_captcha(time_form_in_response)
        solution = await self._solver.solve(captcha)
        info = self._info_getter.get_person_info()

        response = await self._ddoser.send_final_form(solution, hidden_fields, info)

        return self._extractor.check_success(response)

    async def notify_subscribers(self, message):
        await self._bot.notify_subscribers(message)

    async def _check_free_places(self, formatted_date: str) -> str:
        response = await self._ddoser.get_month(formatted_date, self._solver.get_last_solution())
        if response:
            if (not self._extractor.check_success(response)) and self._solver.get_last_solution():
                await self._solver.report_incorrect()
            if await self._captcha_solved(response):
                return ''

            return self._extractor.extract_day_href(response)

        return ''

    async def _captcha_solved(self, response):
        captcha = self._extractor.extract_captcha(response)
        if captcha:
            solution = await self._solver.solve(captcha)
            if solution:
                self._captcha_solution = solution
            else:
                return False
        return bool(captcha)
