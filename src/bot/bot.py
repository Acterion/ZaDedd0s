import logging

from aiogram import Bot, Dispatcher, executor, types

import src.bot.menu as menu

import src.backend.backend as backend

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


class DDBot:
    def __init__(self, token):
        self._bot = Bot(token)
        self._dp = Dispatcher(self._bot)
        self._backend = backend.Backend(self)
        self._menu = menu.Menu(self._bot, self._backend)

    def add_handlers(self):
        """Add commands and message handlers."""
        self._dp.register_message_handler(self._menu.open_keyboard, commands=['start'])
        self._menu.add_handlers(self._dp)
        self._dp.register_message_handler(self.echo)

    def start_bot(self):
        """Start the bot."""
        self.add_handlers()
        executor.start_polling(self._dp, skip_updates=True)

    def echo(self, update, context):
        """Echo the user message."""
        self.notify_subscribers(update.message.text)
        # update.message.reply_text(update.message.text)

    def notify_subscribers(self, message):
        """Broadcast message to all subs."""
        for sub in self._menu.get_subs():
            self._bot.send_message(sub, message)
