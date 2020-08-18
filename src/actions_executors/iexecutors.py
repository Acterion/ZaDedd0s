import abc
from collections import namedtuple

PersonInfo = namedtuple('PersonInfo', 'name surname email residence passport')


class IDdoser(abc.ABC):
    @abc.abstractmethod
    async def get_month(self, date: str, solved_captcha: str = None) -> str:
        pass

    @abc.abstractmethod
    async def get_day(self, day_href: str) -> str:
        pass

    @abc.abstractmethod
    async def get_time_slot(self, time_href: str) -> str:
        pass

    @abc.abstractmethod
    async def send_final_form(self, solved_captcha: str, hidden_fields: dict, person_info: PersonInfo) -> str:
        pass


class IHtmlExtractor(abc.ABC):
    @abc.abstractmethod
    def extract_captcha(self, html: str) -> str:
        pass

    @abc.abstractmethod
    def extract_day_href(self, html: str) -> str:
        pass

    @abc.abstractmethod
    def extract_time_href(self, html: str) -> str:
        pass

    @abc.abstractmethod
    def extract_hidden_fields(self, html: str) -> dict:
        pass

    @abc.abstractmethod
    def check_success(self, html: str) -> bool:
        pass


class ITelegramBot(abc.ABC):
    @abc.abstractmethod
    async def notify_subscribers(self, message: str):
        pass


class ICaptchaSolver(abc.ABC):
    @abc.abstractmethod
    async def solve(self, captcha: str) -> str:
        pass

    @abc.abstractmethod
    def get_last_solution(self) -> str:
        pass
