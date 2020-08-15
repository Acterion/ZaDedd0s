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
