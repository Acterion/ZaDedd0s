from aiogram import Bot, Dispatcher, types


class Menu:
    def __init__(self, bot: Bot, backend):
        self._subs = set()
        self._bot = bot
        self._backend = backend

    def get_subs(self):
        return self._subs

    def add_handlers(self, disp: Dispatcher):
        disp.register_message_handler(self.help, text='Help')
        disp.register_message_handler(self.close_keyboard, text='Close')
        disp.register_message_handler(self.start, text='Start')
        disp.register_message_handler(self.stop, text='Stop')
        disp.register_message_handler(self.report, text='Report')
        disp.register_message_handler(self.subscribe, text='Subscribe')
        disp.register_message_handler(self.list_subs, text='List subs')

    async def start(self, message: types.Message):
        """Start ddos when the command Start is issued."""
        await message.answer('Starting ddos')
        self._backend.start_machine()

    async def stop(self, message: types.Message):
        """Stop ddos when the command Stop is issued."""
        await message.answer('Stopping ddos')
        self._backend.stop_machine()

    async def help(self, message: types.Message):
        """Send a message when the command /help or Help is issued."""
        await message.answer('Use /start to display control panel')

    async def report(self, message: types.Message):
        """Send report message."""
        await message.answer('Please wait, while we prepare your report...')
        await message.answer(await self._backend.get_report())

    async def subscribe(self, message: types.Message):
        """Add user to subs set"""
        if message.chat.id not in self._subs:
            self._subs.add(message.chat.id)
            await message.answer('You successfully subscribed to reports!')
        else:
            await message.answer('You have already subscribed to reports!')

    async def list_subs(self, message: types.Message):
        """Send list of current subs."""
        all_subs = ", ".join(f"{n}" for n in self._subs)
        reply = "No subs" if not all_subs else all_subs
        await message.answer(reply)

    async def open_keyboard(self, message: types.Message):
        """Open reply keyboard."""
        await message.answer(
            text="Opening custom keyboard",
            reply_markup=self.main_menu_keyboard_reply()
        )

    @staticmethod
    async def close_keyboard(message: types.Message):
        """Close reply keyboard."""
        await message.answer(
            text="Closing keyboard",
            reply_markup=types.ReplyKeyboardRemove()
        )

    @staticmethod
    def main_menu_keyboard_reply():
        keyboard_markup = types.ReplyKeyboardMarkup(row_width=2)
        buttons = ('Help', 'Close',
                   'Start', 'Stop',
                   'Report', 'Subscribe',
                   'List subs')
        keyboard_markup.add(*(types.KeyboardButton(text) for text in buttons))

        return keyboard_markup
