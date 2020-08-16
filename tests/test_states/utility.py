from src.states.istate import IState


class FFinalState(IState):
    def __init__(self):
        self.run_was_called = False

    async def run(self):
        self.run_was_called = True

    def run_was_called(self) -> bool:
        return self.run_was_called

    def next(self):
        pass
