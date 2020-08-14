from src.event_loop.event_loop import Loop


class StateMachine:
    def __init__(self, initial_state):
        self._current_state = initial_state
        self._loop = Loop()

    def exec(self):
        self._loop.run_until_complete(self._exec_impl)

    async def _exec_impl(self):
        while self._current_state:
            await self._proceed_state()

    async def _proceed_state(self):
        await self._current_state.run()
        self._current_state = self._current_state.next()
