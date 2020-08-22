from src.stat.stat import StatisticsCollector
from src.stat.data import StatData, Report
import time
from unittest import mock


class MStatisticsCollector(StatisticsCollector):
    async def get_balance(self):
        time.sleep(1)
        return 9.9944

    def load_key(self):
        return None


prefilled_stat_data = StatData('test_stat_filled.txt')

prefilled_report = Report(7, 5, 6, 9.9944, 4, "Up", round(time.time()) - 999, 1, 2)

filled = '''{
    "avg_captcha_count": 1,
    "avg_day_cost": 2,
    "balance": 3,
    "current_state": true,
    "page_updates": 4,
    "rejected": 5,
    "spent": 6,
    "total_captcha_count": 7,
    "uptime": 1000,
    "uptime_captcha_count": 8,
    "uptime_end": 2000,
    "uptime_spent": 9,
    "uptime_start": 1000
}'''