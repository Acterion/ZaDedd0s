import pytest

from src.actions_executors.solver import Solver
from src.statistics.istatistics import ISolverStatistics
from src.utils.file_utils import read_file
import tests.test_solver.samples as samples


class MSolverStatistics(ISolverStatistics):

    def add_captcha(self, cost, solved):
        pass


@pytest.mark.asyncio
async def closed_test_solve_captcha():
    key = read_file('captcha_token.txt')
    solver = Solver(MSolverStatistics(), key)
    solution = await solver.solve(samples.captcha_sample)
    assert solution == "nwd47p"
