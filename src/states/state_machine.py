import abc
import asyncio
import atexit
from datetime import datetime
from asyncio import AbstractEventLoop
from src.statistics.istatistics import IMachineStatistics


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
    def __init__(self, initial_state, loop: AbstractEventLoop, stat: IMachineStatistics):
        self._current_state = initial_state
        self._loop = loop
        self._stat = stat
        self._is_running = False
        self._exec_feature = None
        atexit.register(self.cleanup)

    def cleanup(self):
        self._stat.register_downtime()

    def is_running(self):
        return self._is_running

    def stop(self):
        print(datetime.now(), " Spooling down the machine...")
        self._is_running = False
        self._exec_feature.cancel()
        self._stat.register_downtime()

    def start(self):
        print(datetime.now(), " Spooling up the machine!")
        self._is_running = True
        self._exec_feature = asyncio.ensure_future(self._exec(), loop=self._loop)
        self._stat.register_uptime()

    async def _exec(self):
        while self._current_state and self._is_running:
            await self._proceed_state()

    async def _proceed_state(self):
        await self._current_state.run()
        self._current_state = self._current_state.next()
