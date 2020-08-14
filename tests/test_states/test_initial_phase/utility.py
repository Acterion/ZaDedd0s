from src.states.istate_actions import IStateActions
from src.states.istate import AErrorState


class FakeStateActions(IStateActions):
    def __init__(self, network_error=False):
        self._get_current_month_and_solve_captcha_was_called_once = False
        self._network_error = network_error

    async def get_current_month_and_solve_captcha(self):
        if self._network_error:
            raise RuntimeError()

        self._get_current_month_and_solve_captcha_was_called_once = True

    async def detect_free_places(self): pass

    def assert_get_current_month_and_solve_captcha_was_called_once(self):
        assert self._get_current_month_and_solve_captcha_was_called_once


class FakeError(AErrorState):
    def __init__(self):
        self._finalize_was_called = False

    def finalize(self):
        self._finalize_was_called = True

    def assert_finalize_was_called(self):
        assert self._finalize_was_called
