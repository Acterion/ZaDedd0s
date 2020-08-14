import abc


class IStateActions(abc.ABC):
    @abc.abstractmethod
    async def get_current_month_and_solve_captcha(self):
        pass

    @abc.abstractmethod
    async def detect_free_places(self):
        pass
