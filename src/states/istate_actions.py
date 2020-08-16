import abc


class IStateActions(abc.ABC):
    @abc.abstractmethod
    async def get_current_month_and_solve_captcha(self):
        pass

    @abc.abstractmethod
    async def check_free_places_in_current_month(self) -> bool:
        pass

    @abc.abstractmethod
    async def check_free_places_in_next_month(self) -> bool:
        pass

    @abc.abstractmethod
    async def try_to_reserve_place(self) -> bool:
        pass

    @abc.abstractmethod
    async def notify_subscribers(self, message):
        pass


class ActionError(RuntimeError):
    def __init__(self, error_info):
        self.info = error_info

    def __str__(self):
        return self.info
