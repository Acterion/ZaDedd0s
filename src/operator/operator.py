import abc
from datetime import datetime, timedelta, time

from dateutil.relativedelta import relativedelta

from src.scheduler.scheduler import IScheduler
from src.states.state_machine import IStateMachine
from src.statistics.istatistics import IOperatorStatistics


def default_machine_stop_and_start_time(start_time_hour=8, uptime_duration_hours=12, now: datetime = datetime.now()):
    return now.replace(hour=start_time_hour) + relativedelta(hours=uptime_duration_hours), \
           now.replace(hour=start_time_hour) + relativedelta(days=1)


class IOperatorClocks(abc.ABC):
    @abc.abstractmethod
    def shutdown_and_next_start_times(self, real_start_time: time) -> (datetime, datetime):
        pass


class OperatorClocks(IOperatorClocks):
    def __init__(self, start_time_hour=8, uptime_duration_hours=12, now: datetime = datetime.now()):
        self._current_start_time = datetime.now().replace(hour=start_time_hour)
        self._shutdown_time, self._next_start_time = default_machine_stop_and_start_time(start_time_hour,
                                                                                         uptime_duration_hours, now)

    def shutdown_and_next_start_times(self, real_start_time: time) -> (datetime, datetime):
        print(f'real {real_start_time}, up {self._current_start_time.time()}, down {self._shutdown_time.time()}')
        # if real_start_time >= self._shutdown_time.time() or real_start_time <= self._current_start_time.time():
        #     raise RuntimeError('F*ck you!')
        return self._shutdown_time, self._next_start_time


class Operator:
    def __init__(self, scheduler: IScheduler, machine: IStateMachine, clocks: IOperatorClocks,
                 stat: IOperatorStatistics):
        self._scheduler = scheduler
        self._machine = machine
        self._clocks = clocks
        self._stat = stat

        self._start_time = None
        self._stop_time = None
        self._starter = None
        self._stopper = None

    def start_machine(self):
        self._machine.start()
        self._stop_time, self._start_time = self._clocks.shutdown_and_next_start_times(datetime.now().time())
        self._stopper = self._scheduler.schedule(self._stop_time, self._machine.stop)
        self._starter = self._scheduler.schedule(self._start_time, self._machine.start)
        self._stat.register_uptime()

    def stop_machine(self):
        self._machine.stop()
        self._starter.cancel()
        self._stat.register_downtime()
