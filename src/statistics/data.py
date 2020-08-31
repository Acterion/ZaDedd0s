import json
import time
from collections import namedtuple
from src.utils.file_utils import read_json, write_file

Report = namedtuple('Report', 'captcha_count rejected_captcha_count spent balance '
                              'page_updates current_state uptime avg_captcha_count '
                              'avg_day_cost')


class StatData:
    def __init__(self, path='stat.txt'):
        j = json.loads(read_json(path))
        self.total_captcha_count = j.get('total_captcha_count', 0)
        self.uptime_captcha_count = j.get('uptime_captcha_count', 0)
        self.rejected = j.get('rejected', 0)
        self.spent = j.get('spent', 0)
        self.uptime_spent = j.get('uptime_spent', 0)
        self.balance = j.get('balance', 0)
        self.page_updates = j.get('page_updates', 0)
        self.current_state = j.get('current_state', 0)
        self.uptime_start = j.get('uptime_start', 0)
        self.uptime = j.get('uptime', 0)
        self.uptime_end = j.get('uptime_end', 0)
        self.avg_captcha_count = j.get('avg_captcha_count', 0)
        self.avg_day_cost = j.get('avg_day_cost', 0)

    def save_stat(self, path='stat.txt'):
        write_file(path, json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4))

    def get_report(self) -> Report:
        if self.current_state:
            state = "Up"
            self.uptime = round(time.time()) - self.uptime_start
        else:
            state = "Down"

        report = Report(
            self.total_captcha_count,
            self.rejected,
            self.spent,
            self.balance,
            self.page_updates,
            state,
            self.uptime,
            self.avg_captcha_count,
            self.avg_day_cost
        )
        return report
