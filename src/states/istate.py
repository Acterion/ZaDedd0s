import abc


class IState(abc.ABC):
    @abc.abstractmethod
    def run(self):
        pass

    @abc.abstractmethod
    def next(self):
        pass


class AState(IState, abc.ABC):
    def __init__(self, state_actions, next_states, error_state):
        self._state_actions = state_actions
        self._next_state = None
        self._next_states = next_states
        self._error_state = error_state

    async def run(self):
        try:
            await self.call_actions()
            self._next_state = self.select_next_state()
        except RuntimeError:
            self._next_state = self._error_state

    def next(self):
        return self._next_state

    def set_next_states(self, next_states):
        self._next_states = next_states

    def select_next_state(self, state_name=None):
        if not self._next_states:
            return None
        if not state_name:
            return next(iter(self._next_states.values()))
        if state_name and state_name in self._next_states:
            return self._next_states[state_name]

    @abc.abstractmethod
    async def call_actions(self):
        pass


class AErrorState(IState):
    async def run(self):
        self.finalize()

    def next(self):
        pass

    def finalize(self):
        pass
