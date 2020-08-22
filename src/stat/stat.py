import aiohttp
import json
import os
import time
from collections import namedtuple

from src.utils.file_utils import read_file, write_file

Report = namedtuple('Report', 'captcha_count rejected_captcha_count spent balance '
                              'page_updates current_state uptime avg_captcha_count '
                              'avg_day_cost')


class StatData:
    def __init__(self, path=None, total_captcha_count=0, uptime_captcha_count=0, rejected=0,
                 spent=0, uptime_spent=0, balance=0, page_updates=0, current_state=False, uptime_start=0,
                 uptime=0, uptime_end=0, avg_captcha_count=0, avg_day_cost=0):
        self.total_captcha_count = total_captcha_count
        self.uptime_captcha_count = uptime_captcha_count
        self.rejected = rejected
        self.spent = spent
        self.uptime_spent = uptime_spent
        self.balance = balance
        self.page_updates = page_updates
        self.current_state = current_state
        self.uptime_start = uptime_start
        self.uptime = uptime
        self.uptime_end = uptime_end
        self.avg_captcha_count = avg_captcha_count
        self.avg_day_cost = avg_day_cost
        if path:
            self.load_stat(path)

    def load_stat(self, path):
        j = json.loads(read_file(path))
        self.total_captcha_count = j.get('total_captcha_count')
        self.uptime_captcha_count = j.get('uptime_captcha_count')
        self.rejected = j.get('rejected')
        self.spent = j.get('spent')
        self.uptime_spent = j.get('uptime_spent')
        self.balance = j.get('balance')
        self.page_updates = j.get('page_updates')
        self.current_state = j.get('current_state')
        self.uptime_start = j.get('uptime_start')
        self.uptime = j.get('uptime')
        self.uptime_end = j.get('uptime_end')
        self.avg_captcha_count = j.get('avg_captcha_count')
        self.avg_day_cost = j.get('avg_day_cost')

    def save_stat(self, path):
        write_file(path, json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4))


class StatisticsCollector:
    def __init__(self, stat_data=StatData()):
        self._stat = stat_data
        self._client_key = read_file(os.environ['captcha_user_key'])

    def save(self, path='stat.txt'):
        self._stat.save_stat(path)

    def load(self, path='stat.txt'):
        self._stat.load_stat(path)

    def get_stat(self) -> StatData:
        return self._stat

    def add_captcha(self, cost, solved):
        self._stat.uptime_captcha_count += 1
        self._stat.total_captcha_count += 1
        if not solved:
            self._stat.rejected += 1
        self._stat.uptime_spent += cost
        self._stat.spent += cost

    def add_page_update(self):
        self._stat.page_updates += 1

    async def get_balance(self):
        balance_url = 'https://api.anti-captcha.com/getBalance'
        payload = {'clientKey': self._client_key}
        async with aiohttp.ClientSession() as session:
            async with session.post(balance_url, json=payload) as resp:
                return (await resp.json())['balance']

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

    async def get_report(self) -> Report:
        if self._stat.current_state:
            self._stat.current_state = "Up"
            self._stat.uptime = round(time.time()) - self._stat.uptime_start
        else:
            self._stat.current_state = "Down"

        self._stat.balance = await self.get_balance()

        report = Report(
            self._stat.total_captcha_count,
            self._stat.rejected,
            self._stat.spent,
            self._stat.balance,
            self._stat.page_updates,
            self._stat.current_state,
            self._stat.uptime,
            self._stat.avg_captcha_count,
            self._stat.avg_day_cost
        )
        return report
