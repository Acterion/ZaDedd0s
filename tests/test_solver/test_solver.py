import pytest

from src.actions_executors.solver import Solver
import tests.test_solver.samples as samples


@pytest.mark.asyncio
async def closed_test_solve_captcha():
    solver = Solver()
    solution = await solver.solve(samples.captcha_sample)
    assert solution == "nwd47p"
