from asyncio.events import TimerHandle
from datetime import datetime
from unittest.mock import call

from src.operator.operator import Operator, default_machine_stop_and_start_time
from src.scheduler.scheduler import IScheduler
from src.states.state_machine import IStateMachine


class MScheduler(IScheduler):
    def __init__(self, mocker):
        mocker.patch.object(self, 'schedule')

    def schedule(self, when: datetime, callback, *args) -> TimerHandle:
        pass


class MStateMachine(IStateMachine):
    def __init__(self, mocker):
        mocker.patch.object(self, 'is_running')
        mocker.patch.object(self, 'start')
        mocker.patch.object(self, 'stop')

    def is_running(self):
        pass

    def start(self):
        pass

    def stop(self):
        pass


def test_machine_start(mocker):
    scheduler = MScheduler(mocker)
    machine = MStateMachine(mocker)
    stop, start = default_machine_stop_and_start_time()

    operator = Operator(scheduler, machine)
    operator.start_machine()

    machine.start.assert_called_once()
    assert scheduler.schedule.call_args_list == [call(stop, machine.stop), call(start, machine.start)]


def test_machine_stop(mocker):
    machine = MStateMachine(mocker)
    operator = Operator(MScheduler(mocker), machine)

    operator.stop_machine()

    machine.stop.assert_called_once()
