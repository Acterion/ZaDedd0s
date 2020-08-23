from src.statistics.istatistics import IReporter, IOperatorStatistics, ISolverStatistics, IDdoserStatistics, Report


class StatisticsCollector(IReporter, IOperatorStatistics, ISolverStatistics, IDdoserStatistics):
    async def get_report(self) -> Report:
        pass

    def register_uptime(self):
        pass

    def register_downtime(self):
        pass

    def add_captcha(self, cost, solved):
        pass

    def add_page_update(self):
        pass
