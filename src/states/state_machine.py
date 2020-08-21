from asyncio import AbstractEventLoop


class StateMachine:
    def __init__(self, initial_state, loop: AbstractEventLoop):
        self._current_state = initial_state
        self._loop = loop
        self._is_running = False

    def running(self):
        return self._is_running

    def shutdown(self):
        self._is_running = False

    def start(self):
        self._is_running = True
        self._exec()

    def exec(self):
        self._loop.run_until_complete(self._exec_impl)

    async def _exec_impl(self):
        while self._current_state and self._is_running:
            await self._proceed_state()

    async def _proceed_state(self):
        await self._current_state.run()
        self._current_state = self._current_state.next()
