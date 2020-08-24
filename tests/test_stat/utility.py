from src.statistics.statistics import StatisticsCollector
import time


class MStatisticsCollector(StatisticsCollector):
    async def get_balance(self):
        time.sleep(1)
        return 9.9944

    def load_key(self):
        return None


filled_dict = {
    "avg_captcha_count": 1,
    "avg_day_cost": 2,
    "balance": 3,
    "current_state": True,
    "page_updates": 4,
    "rejected": 5,
    "spent": 6,
    "total_captcha_count": 7,
    "uptime": 1000,
    "uptime_captcha_count": 8,
    "uptime_end": 2000,
    "uptime_spent": 9,
    "uptime_start": 1000
}


filled_json = '''{
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

empty_json = '''{
    "avg_captcha_count": 0,
    "avg_day_cost": 0,
    "balance": 0,
    "current_state": false,
    "page_updates": 0,
    "rejected": 0,
    "spent": 0,
    "total_captcha_count": 0,
    "uptime": 0,
    "uptime_captcha_count": 0,
    "uptime_end": 0,
    "uptime_spent": 0,
    "uptime_start": 0
}'''