import asyncio
from asyncio import AbstractEventLoop
from datetime import datetime

from dateutil.relativedelta import relativedelta

from src.scheduler.scheduler import Scheduler


class Clazz:
    def __init__(self, loop: AbstractEventLoop):
        self.method_was_call_at = None
        self._loop = loop

    def method(self):
        self.method_was_call_at = round(datetime.now().timestamp())
        self._loop.stop()


def test_sth():
    loop = asyncio.get_event_loop()
    clazz = Clazz(loop)
    scheduler = Scheduler(loop)

    next_second = datetime.now() + relativedelta(microseconds=100)
    scheduler.schedule(next_second, clazz.method)
    loop.run_forever()

    assert clazz.method_was_call_at == round(next_second.timestamp())

