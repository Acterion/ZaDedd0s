import abc
import asyncio
from asyncio import AbstractEventLoop


class IStateMachine(abc.ABC):
    @abc.abstractmethod
    def is_running(self):
        pass

    @abc.abstractmethod
    def start(self):
        pass

    @abc.abstractmethod
    def stop(self):
        pass


class StateMachine(IStateMachine):
    def __init__(self, initial_state, loop: AbstractEventLoop):
        self._current_state = initial_state
        self._loop = loop
        self._is_running = False

    def is_running(self):
        return self._is_running

    def stop(self):
        self._is_running = False

    def start(self):
        self._is_running = True
        asyncio.ensure_future(self._exec(), loop=self._loop)

    async def _exec(self):
        while self._current_state and self._is_running:
            await self._proceed_state()

    async def _proceed_state(self):
        await self._current_state.run()
        self._current_state = self._current_state.next()
