import os

import src.utils.file_utils as file_uti
from src.actions_executors.bot import DDBot


def main():
    bot_token = file_uti.readFile(os.environ['bot_token'])
    bot = DDBot(bot_token)
    bot.start_bot()


if __name__ == '__main__':
    main()
