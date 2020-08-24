from telegram import KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove
from telegram.ext import MessageHandler, Filters


class Menu:
    def __init__(self, bot, backend):
        self._subs = set()
        self._bot = bot
        self._backend = backend

    def get_subs(self):
        return self._subs

    def add_handlers(self, disp):
        disp.add_handler(MessageHandler(Filters.regex(r"[Hh]elp"), self.help))
        disp.add_handler(MessageHandler(Filters.regex(r"Close"), self.close_keyboard))
        disp.add_handler(MessageHandler(Filters.regex(r"Start"), self.start))
        disp.add_handler(MessageHandler(Filters.regex(r"Stop"), self.stop))
        disp.add_handler(MessageHandler(Filters.regex(r"report"), self.report))
        disp.add_handler(MessageHandler(Filters.regex(r"Subscribe"), self.subscribe))
        disp.add_handler(MessageHandler(Filters.regex(r"subs"), self.list_subs))

    def start(self, update, context):
        """Start ddos when the command Start is issued."""
        update.message.reply_text('Starting ddos')
        self._backend.start_machine()

    def stop(self, update, context):
        """Stop ddos when the command Stop is issued."""
        update.message.reply_text('Stopping ddos')
        self._backend.stop_machine()

    def help(self, update, context):
        """Send a message when the command /help or Help is issued."""
        update.message.reply_text('Use /key to display control panel')

    async def report(self, update, context):
        """Send report message."""
        update.message.reply_text(self._backend.get_report())

    def subscribe(self, update, context):
        """Add user to subs set"""
        if update.message.chat_id not in self._subs:
            self._subs.add(update.message.chat_id)
            update.message.reply_text('You successfully subscribed to reports!')
        else:
            update.message.reply_text('You have already subscribed to reports!')

    def list_subs(self, update, context):
        """Send list of current subs."""
        all_subs = ", ".join(f"{n}" for n in self._subs)
        reply = "No subs" if not all_subs else all_subs
        update.message.reply_text(reply)

    def open_keyboard(self, update, context):
        """Open reply keyboard."""
        self._bot.send_message(
            chat_id=update.message.chat_id,
            text="Opening custom keyboard",
            reply_markup=self.main_menu_keyboard_reply())

    def close_keyboard(self, update, context):
        """Close reply keyboard."""
        self._bot.send_message(
            chat_id=update.message.chat_id,
            text="Closing keyboard",
            reply_markup=ReplyKeyboardRemove()
        )

    @staticmethod
    def main_menu_keyboard_reply(self):
        keyboard = [[KeyboardButton('Help'), KeyboardButton('Close')],
                    [KeyboardButton('Start'), KeyboardButton('Stop')],
                    [KeyboardButton('Get report'), KeyboardButton('Subscribe')],
                    [KeyboardButton('List subs')]]
        return ReplyKeyboardMarkup(keyboard)
