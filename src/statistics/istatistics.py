import abc

from src.statistics.data import Report


class IReporter(abc.ABC):
    @abc.abstractmethod
    async def get_report(self) -> Report:
        pass


class IMachineStatistics(abc.ABC):
    @abc.abstractmethod
    def register_uptime(self):
        pass

    @abc.abstractmethod
    def register_downtime(self):
        pass


class ISolverStatistics(abc.ABC):
    @abc.abstractmethod
    def add_captcha(self, cost, solved):
        pass


class IDdoserStatistics(abc.ABC):
    @abc.abstractmethod
    def add_page_update(self):
        pass
