import os

import src.utils.file_utils as file_uti
from src.actions_executors.bot import DDBot
from src.operator.operator import Operator


def main():
    bot_token = file_uti.read_file(os.environ['bot_token'])
    # bot = DDBot(bot_token)
    # bot.start_bot()
    o = Operator(None, None, bot_token)


if __name__ == '__main__':
    main()
