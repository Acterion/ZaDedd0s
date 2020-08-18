import abc
from collections import namedtuple

PersonInfo = namedtuple('PersonInfo', 'firstname lastname email residence passport')


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


