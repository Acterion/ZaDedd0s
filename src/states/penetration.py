from src.states.istate import AState


class Penetration(AState):
    def __init__(self, state_actions, next_states, error_state):
        super().__init__(state_actions, next_states, error_state)
        self._reservation_succeeded = False

    async def call_actions(self):
        self._reservation_succeeded = await self._state_actions.try_to_reserve_place()

    def select_next_state(self, name=None):
        if self._reservation_succeeded:
            return super(Penetration, self).select_next_state('success')
        return super(Penetration, self).select_next_state('ddosing')

