import asyncio
import os

from src.operator.operator import Operator, OperatorClocks
from src.scheduler.scheduler import Scheduler
from src.states.state_actions_factory import StateActionsFactory
from src.states.state_machine import StateMachine
from src.states.states_factory import StatesFactory
from src.statistics.statistics import StatisticsCollector
from src.utils.file_utils import read_file


class Backend:
    def __init__(self, bot):
        loop = asyncio.get_event_loop()
        self._scheduler = Scheduler(loop)
        self._statistics_collector = StatisticsCollector()
        self._captcha_client_key = read_file(os.environ['captcha_user_key'])
        actions = StateActionsFactory(bot, self._statistics_collector, self._statistics_collector,
                                      self._captcha_client_key).make_sate_actions()
        initial_state = StatesFactory(actions).make_initial()

        self._operator = Operator(self._scheduler, StateMachine(initial_state, loop), OperatorClocks(),
                                  self._statistics_collector)
        # loop.run_forever()

    def start_machine(self):
        self._operator.start_machine()

    def stop_machine(self):
        self._operator.stop_machine()

    def get_report(self):
        return self._statistics_collector.get_report()
