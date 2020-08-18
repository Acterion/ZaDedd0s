from collections import namedtuple

from src.actions_executors.iexecutors import IDdoser, IHtmlExtractor, ICaptchaSolver, ITelegramBot, PersonInfo
from src.states.state_actions import IPersonInfoGetter, StateActions


class FDdoser(IDdoser):
    def __init__(self):
        self.get_month_was_called_with = ()
        self.get_day_was_called_with = ''
        self.get_time_slot_was_called_with = ''
        self.send_final_form_was_called_with = ()

    async def get_month(self, date: str, solved_captcha: str = None) -> str:
        self.get_month_was_called_with = (date, solved_captcha)
        return '<html> captcha <html>'

    async def get_day(self, day_href: str) -> str:
        self.get_day_was_called_with = day_href
        return 'day form'

    async def get_time_slot(self, time_href: str) -> str:
        self.get_time_slot_was_called_with = time_href
        return 'final form'

    async def send_final_form(self, solved_captcha: str, hidden_fields: dict, person_info: PersonInfo):
        self.send_final_form_was_called_with = (solved_captcha, hidden_fields, person_info)


class MHtmlExtractor(IHtmlExtractor):
    def __init__(self, mocker):
        mocker.patch.object(self, 'extract_captcha')
        mocker.patch.object(self, 'extract_day_href')
        mocker.patch.object(self, 'extract_time_href')
        mocker.patch.object(self, 'extract_hidden_fields')
        mocker.patch.object(self, 'check_success')

    def extract_captcha(self, html: str) -> str: pass
    def extract_day_href(self, html: str) -> str: pass
    def extract_time_href(self, html: str) -> str: pass
    def extract_hidden_fields(self, html: str) -> dict: pass
    def check_success(self, html: str) -> bool: pass


class FCaptchaSolver(ICaptchaSolver):
    def __init__(self):
        self.solve_was_called_with = ''
        self._last_solution = '4u'

    async def solve(self, captcha: str) -> str:
        self.solve_was_called_with = captcha
        return self._last_solution

    def get_last_solution(self) -> str:
        return self._last_solution


class FTelegramBot(ITelegramBot):
    async def notify_subscribers(self, message: str):
        pass


class MPersonInfoGetter(IPersonInfoGetter):
    def __init__(self, mocker):
        mocker.patch.object(self, 'get_person_info')

    def get_person_info(self) -> PersonInfo:
        pass


ActionsAndBoys = namedtuple('ActionsAndBoys', 'actions ddoser extractor bot solver info_getter')


def make_actions_and_boys(mocker) -> ActionsAndBoys:
    ddoser = FDdoser()
    extractor = MHtmlExtractor(mocker)
    bot = FTelegramBot()
    solver = FCaptchaSolver()
    info_getter = MPersonInfoGetter(mocker)
    actions = StateActions(ddoser, extractor, bot, solver, info_getter)
    return ActionsAndBoys(actions, ddoser, extractor, bot, solver, info_getter)
