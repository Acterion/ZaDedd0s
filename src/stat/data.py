import json
import time
from collections import namedtuple
from src.utils.file_utils import read_file, write_file

Report = namedtuple('Report', 'captcha_count rejected_captcha_count spent balance '
                              'page_updates current_state uptime avg_captcha_count '
                              'avg_day_cost')


class StatData:
    def __init__(self, path='stat.txt'):
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

    def get_report(self) -> Report:
        if self.current_state:
            self.current_state = "Up"
            self.uptime = round(time.time()) - self.uptime_start
        else:
            self.current_state = "Down"

        report = Report(
            self.total_captcha_count,
            self.rejected,
            self.spent,
            self.balance,
            self.page_updates,
            self.current_state,
            self.uptime,
            self.avg_captcha_count,
            self.avg_day_cost
        )
        return report
