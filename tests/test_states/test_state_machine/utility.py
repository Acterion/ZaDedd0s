import asyncio
from src.states.istate import IState


class FInitialState(IState):
    def __init__(self, final_state):
        self.next_state = None
        self.final_state = final_state

    async def run(self):
        await asyncio.sleep(0.002)
        self.next_state = self.final_state

    def next(self):
        return self.next_state


class FFinalState(IState):
    def __init__(self):
        self.run_was_called = False

    async def run(self):
        self.run_was_called = True

    def get_run_was_called(self):
        return self.run_was_called

    def next(self): pass


def make_initial_and_final_fake_states():
    final = FFinalState()
    initial = FInitialState(final)
    return initial, final
