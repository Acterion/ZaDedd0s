from src.states.istate import AState


class Ddosing(AState):
    async def call_actions(self):
        actions = self._state_actions
        places_detected = False
        while not places_detected:
            places_detected = await actions.check_free_places_in_current_month() \
                              or await actions.check_free_places_in_next_month()
