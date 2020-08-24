import asyncio

from src.actions_executors.bot import DDBot
from src.operator.operator import Operator, OperatorClocks
from src.scheduler.scheduler import Scheduler
from src.states.state_actions_factory import StateActionsFactory
from src.states.state_machine import StateMachine
from src.states.states_factory import StatesFactory
from src.statistics.statistics import StatisticsCollector


class Backend:
    def __init__(self, bot: DDBot):
        loop = asyncio.get_event_loop()
        self._scheduler = Scheduler(loop)
        self._statistics_collector = StatisticsCollector()
        actions = StateActionsFactory(bot, self._statistics_collector, self._statistics_collector).make_sate_actions()
        initial_state = StatesFactory(actions).make_initial()

        self._operator = Operator(self._scheduler, StateMachine(initial_state, loop), OperatorClocks(),
                                  self._statistics_collector)

    def start_machine(self):
        self._operator.start_machine()

    def stop_machine(self):
        self._operator.stop_machine()

    async def get_report(self):
        return await self._statistics_collector.get_report()
