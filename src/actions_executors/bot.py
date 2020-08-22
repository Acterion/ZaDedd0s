import logging

from telegram import Bot
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

import src.bot.menu as menu

from src.actions_executors.iexecutors import ITelegramBot

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


class DDBot(ITelegramBot):
    def __init__(self, token):
        self._bot = Bot(token)
        self._updater = Updater(token, use_context=True)
        self._dp = self._updater.dispatcher
        self._menu = menu.Menu(self._bot)

    def add_handlers(self):
        """Add commands and message handlers."""
        self._dp.add_handler(CommandHandler("key", self._menu.open_keyboard))
        self._menu.add_handlers(self._dp)
        self._dp.add_handler(MessageHandler(Filters.text & ~Filters.command, self.echo))

    def start_bot(self):
        """Start the bot."""
        self.add_handlers()
        self._updater.start_polling()
        self._updater.idle()

    def echo(self, update, context):
        """Echo the user message."""
        self.notify_subscribers(update.message.text)
        # update.message.reply_text(update.message.text)

    def notify_subscribers(self, message):
        """Broadcast message to all subs."""
        for sub in self._menu.get_subs():
            self._bot.send_message(sub, message)
