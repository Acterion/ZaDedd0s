from src.statistics.istatistics import IReporter, IOperatorStatistics, ISolverStatistics, IDdoserStatistics, Report

import os
import time

from src.utils.file_utils import read_file
from src.utils.network_utils import post
from src.statistics.data import StatData


class StatisticsCollector(IReporter, IOperatorStatistics, ISolverStatistics, IDdoserStatistics):
    def __init__(self, path='stat.txt'):
        self._stat = None
        self.load(path)
        self._client_key = self.load_key()

    @staticmethod
    def load_key():
        key = read_file(os.environ['captcha_user_key'])
        return key

    def save(self, path='stat.txt'):
        self._stat.save_stat(path)

    def load(self, path='stat.txt'):
        self._stat = StatData(path)

    def get_stat(self) -> StatData:
        return self._stat

    def add_captcha(self, cost, solved):
        self._stat.uptime_captcha_count += 1
        self._stat.total_captcha_count += 1
        if not solved:
            self._stat.rejected += 1
        self._stat.uptime_spent += cost
        self._stat.spent += cost
        self._stat.balance -= cost

    def add_page_update(self):
        self._stat.page_updates += 1

    async def get_balance(self):
        balance_url = 'https://api.anti-captcha.com/getBalance'
        payload = {'clientKey': self._client_key}
        return (await post(balance_url, json_payload=payload))['balance']

    def register_uptime(self):
        self._stat.current_state = True
        self._stat.uptime_start = round(time.time())
        self._stat.uptime_captcha_count = 0
        self._stat.uptime_spent = 0

    def register_downtime(self):
        self._stat.current_state = False
        self._stat.uptime_end = round(time.time())
        self._stat.uptime = self._stat.uptime_end - self._stat.uptime_start
        self._stat.avg_captcha_count = self._stat.uptime_captcha_count / self._stat.uptime
        self._stat.avg_day_cost = (self._stat.avg_day_cost + self._stat.uptime_spent) / 2

    async def get_report(self):
        self._stat.balance = await self.get_balance()
        return self._stat.get_report()
