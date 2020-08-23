from asyncio.events import TimerHandle
from datetime import datetime
from unittest.mock import call

from src.operator.operator import Operator, default_machine_stop_and_start_time, OperatorClocks, IOperatorClocks
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


class MClocks(IOperatorClocks):
    def __init__(self, mocker):
        mocker.patch.object(self, 'shutdown_and_next_start_times')

    def shutdown_and_next_start_times(self, real_start_time: datetime) -> (datetime, datetime):
        pass


def test_machine_start(mocker):
    clocks = MClocks(mocker)
    scheduler = MScheduler(mocker)
    machine = MStateMachine(mocker)
    stop, start = default_machine_stop_and_start_time()
    clocks.shutdown_and_next_start_times.return_value = (stop, start)

    operator = Operator(scheduler, machine, clocks)
    operator.start_machine()

    machine.start.assert_called_once()
    assert scheduler.schedule.call_args_list == [call(stop, machine.stop), call(start, machine.start)]


def test_machine_stop(mocker):
    machine = MStateMachine(mocker)
    operator = Operator(MScheduler(mocker), machine, MClocks(mocker))

    operator.stop_machine()

    machine.stop.assert_called_once()
