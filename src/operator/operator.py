from datetime import datetime, timedelta

from dateutil.relativedelta import relativedelta

from src.scheduler.scheduler import IScheduler
from src.states.state_machine import IStateMachine


def default_machine_stop_and_start_time(start_time_hour=8, uptime_duration_hours=12, now: datetime = datetime.now()):
    return now.replace(hour=start_time_hour) + relativedelta(hours=uptime_duration_hours), \
           now.replace(hour=start_time_hour) + relativedelta(days=1)


class OperatorClocks:
    def __init__(self, start_time_hour=8, uptime_duration_hours=12, now: datetime = datetime.now()):
        self._shutdown_time, self._next_start_time = default_machine_stop_and_start_time(start_time_hour,
                                                                                         uptime_duration_hours, now)

    def shutdown_and_next_start_times(self, real_start_time: datetime) -> (datetime, datetime):
        if real_start_time >= self._shutdown_time:
            raise RuntimeError('F*ck you!')
        return self._shutdown_time, self._next_start_time


class Operator:
    def __init__(self, scheduler: IScheduler, machine: IStateMachine):
        self._scheduler = scheduler
        self._machine = machine
        self._clocks = OperatorClocks()

        self._start_time = None
        self._stop_time = None
        self._starter = None
        self._stopper = None

    def start_machine(self):
        self._machine.start()
        self._stop_time, self._start_time = self._clocks.shutdown_and_next_start_times(datetime.now())
        self._stopper = self._scheduler.schedule(self._stop_time, self._machine.stop)
        self._starter = self._scheduler.schedule(self._start_time, self._machine.start)

    def stop_machine(self):
        self._machine.stop()
