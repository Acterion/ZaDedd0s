from src.stat.stat import StatData, StatisticsCollector, Report
import time

prefilled_stat_data = StatData(None, 7, 8, 5, 6, 9, 3, 4, True, 1000, 1000, 2000, 1, 2)

prefilled_statistics_collector = StatisticsCollector(prefilled_stat_data)

prefilled_report = Report(7, 5, 6, 9.9944, 4, "Up", round(time.time()) - 1000, 1, 2)

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