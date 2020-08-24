from src.utils.file_utils import read_file, write_file
import tests.test_stat.utility as samples
from tests.test_stat.utility import MStatisticsCollector
import time
import pytest


def test_load(mocker):
    mocker.patch('src.statistics.data.read_file', return_value=samples.filled_json)
    stat = MStatisticsCollector()

    assert stat.get_stat().__dict__ == samples.filled_dict


def closed_test_save():
    write_file('test_stat_temp.txt', '')
    stat = MStatisticsCollector('test_stat_filled.txt')
    stat.save('test_stat_temp.txt')

    assert read_file('test_stat_temp.txt') == samples.filled_json


def test_register_uptime(mocker):
    mocker.patch('src.statistics.data.read_file', return_value=samples.empty_json)
    stat = MStatisticsCollector()

    assert not stat.get_stat().current_state
    stat.register_uptime()
    assert stat.get_stat().current_state
    assert stat.get_stat().uptime_start == round(time.time())


def test_register_downtime(mocker):
    mocker.patch('src.statistics.data.read_file', return_value=samples.filled_json)
    stat = MStatisticsCollector()

    assert stat.get_stat().current_state
    stat.register_downtime()
    uptime = round(time.time()) - samples.filled_dict['uptime_start']
    assert not stat.get_stat().current_state
    sd = stat.get_stat()
    assert sd.uptime == uptime
    assert sd.avg_captcha_count == samples.filled_dict['uptime_captcha_count'] / uptime
    assert sd.avg_day_cost == (samples.filled_dict['avg_day_cost'] +
                               samples.filled_dict['uptime_spent']) / 2


def test_add_solved_captcha(mocker):
    mocker.patch('src.statistics.data.read_file', return_value=samples.filled_json)
    stat = MStatisticsCollector()

    stat.add_captcha(1, True)
    sd = stat.get_stat()
    assert sd.uptime_captcha_count == 9
    assert sd.total_captcha_count == 8
    assert sd.rejected == 5
    assert sd.uptime_spent == 10
    assert sd.spent == 7


def test_add_rejected_captcha(mocker):
    mocker.patch('src.statistics.data.read_file', return_value=samples.filled_json)
    stat = MStatisticsCollector()

    stat.add_captcha(1, False)
    sd = stat.get_stat()
    assert sd.uptime_captcha_count == 9
    assert sd.total_captcha_count == 8
    assert sd.rejected == 6
    assert sd.uptime_spent == 10
    assert sd.spent == 7


@pytest.mark.asyncio
async def test_get_report(mocker):
    mocker.patch('src.statistics.data.read_file', return_value=samples.filled_json)
    stat = MStatisticsCollector()

    assert (await stat.get_report()).balance == 9.9944
    assert (await stat.get_report()).uptime == round(time.time()) - 1000


@pytest.mark.asyncio
async def closed_test_get_balance(mocker):
    mocker.patch('src.statistics.data.read_file', return_value=samples.filled_json)
    stat = MStatisticsCollector()
    assert stat.get_balance() == 9.9944
