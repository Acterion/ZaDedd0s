import abc
from datetime import datetime, timedelta, time

from dateutil.relativedelta import relativedelta

from src.scheduler.scheduler import IScheduler
from src.states.state_machine import IStateMachine
from src.statistics.istatistics import IMachineStatistics


def default_machine_stop_and_start_time(start_time_hour=8, uptime_duration_hours=12, now: datetime = datetime.now()):
    return now.replace(hour=start_time_hour + uptime_duration_hours, minute=0) \
           + (relativedelta(days=1) if now.hour >= start_time_hour + uptime_duration_hours else relativedelta()), \
           now.replace(hour=start_time_hour, minute=0) + (relativedelta(days=1)
                                                          if now.hour >= start_time_hour else relativedelta()), \
           now.replace(hour=start_time_hour) <= now < now.replace(hour=start_time_hour + uptime_duration_hours)


class IOperatorClocks(abc.ABC):
    @abc.abstractmethod
    def shutdown_and_next_start_times(self, real_start_time: datetime) -> (datetime, datetime):
        pass


class OperatorClocks(IOperatorClocks):
    def __init__(self, start_time_hour=8, uptime_duration_hours=12, now: datetime = datetime.now()):
        self._current_start_time = datetime.now().replace(hour=start_time_hour, minute=0)
        self._shutdown_time, self._next_start_time, self._start_now = \
            default_machine_stop_and_start_time(start_time_hour,
                                                uptime_duration_hours,
                                                now)

    def shutdown_and_next_start_times(self, real_start_time: datetime) -> (datetime, datetime):
        print(f'real {real_start_time}, up {self._current_start_time}, down {self._shutdown_time}, '
              f'start {self._start_now}')
        # if real_start_time >= self._shutdown_time.time() or real_start_time <= self._current_start_time.time():
        #     raise RuntimeError('F*ck you!')
        return self._shutdown_time, self._next_start_time, self._start_now


class Operator:
    def __init__(self, scheduler: IScheduler, machine: IStateMachine, clocks: IOperatorClocks):
        self._scheduler = scheduler
        self._machine = machine
        self._clocks = clocks

        self._start_time = None
        self._stop_time = None
        self._starter = None
        self._stopper = None

    def start_machine(self):
        # self._machine.start()
        self._stop_time, self._start_time, start_now = self._clocks.shutdown_and_next_start_times(datetime.now())
        if start_now:
            self._machine.start()
        self._stopper = self._scheduler.schedule(self._stop_time, self.stop_machine)
        self._starter = self._scheduler.schedule(self._start_time, self.start_machine)

    def stop_machine(self):
        self._machine.stop()
        self._starter.cancel()
