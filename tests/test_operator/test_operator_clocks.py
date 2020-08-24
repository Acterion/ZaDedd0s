from datetime import datetime, time

import pytest

from src.operator.operator import OperatorClocks


def test_clock_raises_exception_if_too_late():
    clocks = OperatorClocks()
    with pytest.raises(RuntimeError) as _:
        clocks.shutdown_and_next_start_times(time(hour=21))


def test_clock_raises_exception_if_too_early():
    clocks = OperatorClocks()
    with pytest.raises(RuntimeError) as _:
        clocks.shutdown_and_next_start_times(datetime.now().time())


def test_shutdown_and_next_start_times():
    now = datetime.now().replace(hour=10)
    clocks = OperatorClocks(now=now)
    shutdown, start = clocks.shutdown_and_next_start_times(now.time())
    assert shutdown == datetime.now().replace(hour=20)
    assert start == datetime.now().replace(day=datetime.now().day + 1, hour=8)
