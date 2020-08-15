import os


def readFile(path):
    with open(os.environ['bot_token'], "r") as f:
        return f.read()
