from src.states.istate_actions import IStateActions, ActionError
from src.states.final_states import Error


class FakeStateActions(IStateActions):
    def __init__(self, network_error=False,
                 free_places_in_current_month=False, free_places_in_next_month=False,
                 place_reserved=False):
        self.get_current_month_and_solve_captcha_was_called_once = False
        self.check_free_places_in_current_month_was_called_once = False
        self.check_free_places_in_next_month_was_called_once = False
        self.try_to_reserve_place_was_called_once = False
        self.notify_subscribers_was_called_with = ''

        self._network_error = network_error
        self._free_places_in_current_month = free_places_in_current_month
        self._free_places_in_next_month = free_places_in_next_month
        self._place_reserved = place_reserved

    async def get_current_month_and_solve_captcha(self):
        if self._network_error:
            raise ActionError('404')

        self.get_current_month_and_solve_captcha_was_called_once = True

    async def check_free_places_in_current_month(self) -> bool:
        self.check_free_places_in_current_month_was_called_once = True
        return self._free_places_in_current_month

    async def check_free_places_in_next_month(self) -> bool:
        self.check_free_places_in_next_month_was_called_once = True
        return self._free_places_in_next_month

    async def try_to_reserve_place(self) -> bool:
        self.try_to_reserve_place_was_called_once = True
        return self._place_reserved

    async def notify_subscribers(self, message):
        self.notify_subscribers_was_called_with = message
