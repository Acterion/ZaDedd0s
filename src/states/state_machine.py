from src.event_loop.event_loop import Loop


class StateMachine:
    def __init__(self, initial_state):
        self.current_state = initial_state
        self.loop = Loop()

    def exec(self):
        self.loop.run_until_complete(self._exec_impl_)

    async def _exec_impl_(self):
        while self.current_state:
            await self.current_state.run()
            self.current_state = self.current_state.next()
