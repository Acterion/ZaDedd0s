import logging

from telegram import Bot
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


class DDBot:
    def __init__(self, token):
        self._bot = Bot(token)
        self._updater = Updater(token, use_context=True)
        self._dp = self._updater.dispatcher
        self.add_handlers()

    def add_handlers(self):
        """Add commands and message handlers."""
        self._dp.add_handler(CommandHandler("start", self.start))
        self._dp.add_handler(CommandHandler("help", self.help_command))
        self._dp.add_handler(MessageHandler(Filters.text & ~Filters.command, self.echo))

    def start_bot(self):
        """Start the bot."""
        self._updater.start_polling()
        self._updater.idle()

    def start(self, update, context):
        """Send a message when the command /start is issued."""
        update.message.reply_text('Hi!')

    def help_command(self, update, context):
        """Send a message when the command /help is issued."""
        update.message.reply_text('Help!')

    def echo(self, update, context):
        """Echo the user message."""
        self.broadcast_message(update.message.text)
        update.message.reply_text(update.message.text)

    def broadcast_message(self, message):
        """Broadcast message into public channel."""
        self._bot.send_message("@deddoser", message)
