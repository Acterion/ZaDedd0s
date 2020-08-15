from src.states.istate_actions import IStateActions
from src.states.istate import AErrorState


class FakeStateActions(IStateActions):
    def __init__(self, network_error=False, free_places_in_current_month=False, free_places_in_next_month=False):
        self.get_current_month_and_solve_captcha_was_called_once = False
        self.check_free_places_in_current_month_was_called_once = False
        self.check_free_places_in_next_month_was_called_once = False

        self._network_error = network_error
        self._free_places_in_current_month = free_places_in_current_month
        self._free_places_in_next_month = free_places_in_next_month

    async def get_current_month_and_solve_captcha(self):
        if self._network_error:
            raise RuntimeError()

        self.get_current_month_and_solve_captcha_was_called_once = True

    async def check_free_places_in_current_month(self) -> bool:
        self.check_free_places_in_current_month_was_called_once = True
        return self._free_places_in_current_month

    async def check_free_places_in_next_month(self) -> bool:
        self.check_free_places_in_next_month_was_called_once = True
        return self._free_places_in_next_month


class FakeError(AErrorState):
    def __init__(self):
        self._finalize_was_called = False

    def finalize(self):
        self._finalize_was_called = True

    def assert_finalize_was_called(self):
        assert self._finalize_was_called
