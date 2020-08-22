from src.stat.stat import StatisticsCollector
from src.utils.file_utils import read_file, write_file
import tests.test_stat.utility as samples
from tests.test_stat.utility import MStatisticsCollector
import pytest
import time


def test_load():
    stat = MStatisticsCollector('test_stat_filled.txt')
    assert stat.get_stat().__dict__ == samples.prefilled_stat_data.__dict__


def closed_test_save():
    write_file('test_stat_temp.txt', '')
    stat = MStatisticsCollector('test_stat_filled.txt')
    stat.save('test_stat_temp.txt')

    assert read_file('test_stat_temp.txt') == samples.filled


def test_register_uptime():
    stat = MStatisticsCollector('test_stat_empty.txt')

    assert not stat.get_stat().current_state
    stat.register_uptime()
    assert stat.get_stat().current_state
    assert stat.get_stat().uptime_start == round(time.time())


def test_register_downtime():
    stat = MStatisticsCollector('test_stat_filled.txt')

    assert stat.get_stat().current_state
    stat.register_downtime()
    uptime = round(time.time()) - samples.prefilled_stat_data.uptime_start
    assert not stat.get_stat().current_state
    sd = stat.get_stat()
    assert sd.uptime == uptime
    assert sd.avg_captcha_count == samples.prefilled_stat_data.uptime_captcha_count / uptime
    assert sd.avg_day_cost == (samples.prefilled_stat_data.avg_day_cost +
                               samples.prefilled_stat_data.uptime_spent) / 2


def test_add_solved_captcha():
    stat = MStatisticsCollector('test_stat_filled.txt')

    stat.add_captcha(1, True)
    sd = stat.get_stat()
    assert sd.uptime_captcha_count == 9
    assert sd.total_captcha_count == 8
    assert sd.rejected == 5
    assert sd.uptime_spent == 10
    assert sd.spent == 7


def test_add_rejected_captcha():
    stat = MStatisticsCollector('test_stat_filled.txt')

    stat.add_captcha(1, False)
    sd = stat.get_stat()
    assert sd.uptime_captcha_count == 9
    assert sd.total_captcha_count == 8
    assert sd.rejected == 6
    assert sd.uptime_spent == 10
    assert sd.spent == 7


@pytest.mark.asyncio
async def test_get_report():
    stat = MStatisticsCollector('test_stat_filled.txt')
    assert await stat.get_report() == samples.prefilled_report


@pytest.mark.asyncio
async def closed_test_get_balance():
    stat = StatisticsCollector('test_stat_filled.txt')
    assert stat.get_balance() == 9.9944
