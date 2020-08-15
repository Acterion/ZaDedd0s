import os

import src.utils.file_utils as file_uti
import src.bot.bot as bot


def main():
    bot_token = file_uti.readFile(os.environ['bot_token'])
    bot.start_bot(bot_token)


if __name__ == '__main__':
    main()
