from src.actions_executors.bot import DDBot
from src.actions_executors.iexecutors import ITelegramBot


class TelegramBot(ITelegramBot):
    def __init__(self, bot: DDBot):
        self._bot = bot

    async def notify_subscribers(self, message: str):
        self._bot.notify_subscribers(message)
