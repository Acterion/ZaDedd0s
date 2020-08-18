from src.actions_executors.iexecutors import ITelegramBot


class TelegramBot(ITelegramBot):
    def __init__(self, bot):
        self._bot = bot

    async def notify_subscribers(self, message: str):
        self._bot.broadcast_message(message)
