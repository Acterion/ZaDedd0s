import asyncio
import os
import src.utils.file_utils as file_uti
from datetime import datetime, timedelta

from src.scheduler.scheduler import Scheduler
from src.states.state_machine import StateMachine
from src.states.states_factory import StatesFactory
from src.states.state_actions import StateActions
from src.actions_executors.ddoser import Ddoser
from src.actions_executors.html_extractor import HtmlExtractor
from src.actions_executors.bot import DDBot
from src.actions_executors.solver import Solver
from src.states.state_actions import PersonInfoGetter


class Operator:
    def __init__(self, start_time=None,  stop_time=None, bot_token=None):
        self._loop = asyncio.get_event_loop()
        self._start_time = start_time if start_time else datetime.today().replace(hour=8, minute=00, second=00)
        self._stop_time = stop_time if stop_time else self._start_time + timedelta(hours=12)
        self._bot_token = bot_token if bot_token else file_uti.read_file(os.environ['bot_token'])
        self._bot = DDBot(self._bot_token)
        self._bot.start_bot()
        self._s_actions = StateActions(Ddoser(), HtmlExtractor(), self._bot, Solver(), PersonInfoGetter())
        self._s_factory = StatesFactory(self._s_actions)
        self._s_machine = StateMachine(self._s_factory.make_initial(), self._loop)
        self.sch = Scheduler(self._loop)
        self._start_e = self.sch.schedule(self._start_time, self._s_machine.start())
        self._stop_e = self.sch.schedule(self._stop_time, self._s_machine.shutdown())
