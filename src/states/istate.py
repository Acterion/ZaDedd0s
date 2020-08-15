import abc


class IState(ABC):
    @abc.abstractmethod
    def run(self):
        pass

    @abc.abstractmethod
    def next(self):
        pass


class AState(IState, abc.ABC):
    def __init__(self, state_actions, next_state, error_state):
        self._state_actions = state_actions
        self._next_state = next_state
        self._error_state = error_state

    async def run(self):
        try:
            await self.call_actions()
        except RuntimeError:
            self._next_state = self._error_state

    def next(self):
        return self._next_state

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
