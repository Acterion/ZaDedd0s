import abc
from asyncio import AbstractEventLoop, TimerHandle
from datetime import datetime


class IScheduler(abc.ABC):
    @abc.abstractmethod
    def schedule(self, when: datetime, callback, *args) -> TimerHandle:
        pass


class Scheduler(IScheduler):
    def __init__(self, loop: AbstractEventLoop):
        self._loop = loop

    def schedule(self, timestamp: datetime, callback, *args) -> TimerHandle:
        delay = round(timestamp.timestamp() - datetime.now().timestamp())
        return self._loop.call_later(delay, callback, *args)

