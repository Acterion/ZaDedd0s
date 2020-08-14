from src.states.istate import IState


class Ddosing(IState):
    def __init__(self, state_actions):
        self._state_actions = state_actions

    def run(self):
        pass

    def next(self):
        pass


class Initial(IState):
    def __init__(self, state_actions, next_state, error_state):
        self._state_actions = state_actions
        self._next_state = next_state
        self._error_state = error_state

    async def run(self):
        try:
            await self._state_actions.get_current_month_and_solve_captcha()
        except RuntimeError:
            self._next_state = self._error_state

    def next(self):
        return self._next_state
