from datetime import datetime

import pytest

from src.operator.operator import OperatorClocks


def test_call_shutdown_and_next_start_times_not_in_uptime_raises_exception():
    now = datetime(2000, month=10, day=10, hour=10)
    clocks = OperatorClocks(now=now)
    with pytest.raises(RuntimeError) as _:
        clocks.shutdown_and_next_start_times(datetime(2000, month=10, day=10, hour=20))


def test_shutdown_and_next_start_times():
    now = datetime(2000, month=10, day=10, hour=10)
    clocks = OperatorClocks(now=now)
    shutdown, start = clocks.shutdown_and_next_start_times(now)
    assert shutdown == datetime(2000, month=10, day=10, hour=20)
    assert start == datetime(2000, month=10, day=11, hour=8)
