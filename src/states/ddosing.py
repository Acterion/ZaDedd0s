import asyncio
from src.states.istate import AState


class Ddosing(AState):
    def __init__(self, state_actions, next_states, error_state, gap_between_requests=0.01):
        super().__init__(state_actions, next_states, error_state)
        self._gap_between_requests = gap_between_requests

    async def call_actions(self):
        actions = self._state_actions
        places_detected = False
        while not places_detected:
            places_detected = await actions.check_free_places_in_current_month()
            if not places_detected:
                await asyncio.sleep(self._gap_between_requests)
                await actions.check_free_places_in_next_month()
