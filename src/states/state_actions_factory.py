import abc

from src.bot.bot import DDBot
from src.actions_executors.ddoser import Ddoser
from src.actions_executors.html_extractor import HtmlExtractor
from src.actions_executors.solver import Solver
from src.actions_executors.telegram_bot import TelegramBot
from src.states.state_actions import StateActions, PersonInfoGetter
from src.statistics.istatistics import IDdoserStatistics, ISolverStatistics


class IStateActionsFactory(abc.ABC):
    @abc.abstractmethod
    def make_sate_actions(self):
        pass


class StateActionsFactory(IStateActionsFactory):
    def __init__(self, bot: DDBot, ddoser_stat: IDdoserStatistics, solver_stat: ISolverStatistics):
        self._bot = bot
        self._ddoser_stat = ddoser_stat
        self._solver_stat = solver_stat

    def make_sate_actions(self):
        return StateActions(Ddoser(stat=self._ddoser_stat),
                            HtmlExtractor(),
                            TelegramBot(self._bot),
                            Solver(self._solver_stat),
                            PersonInfoGetter())
