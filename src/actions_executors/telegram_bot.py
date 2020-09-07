from src.actions_executors.iexecutors import ITelegramBot


class TelegramBot(ITelegramBot):
    def __init__(self, bot):
        self._bot = bot

    async def notify_subscribers(self, message: str):
        await self._bot.notify_subscribers(message)
