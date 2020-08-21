from asyncio import AbstractEventLoop, TimerHandle


class Scheduler:
    def __init__(self, loop: AbstractEventLoop):
        self._loop = loop

    def schedule(self, timestamp, callback, arg=None) -> TimerHandle:
        handler = self._loop.call_at(timestamp, callback, arg)
        return handler

    def set_timeout(self, delay, callback, arg=None) -> TimerHandle:
        handler = self._loop.call_later(delay, callback, arg)
        return handler

    def exec_now(self, callback, arg=None):
        self._loop.call_soon(callback, arg)
