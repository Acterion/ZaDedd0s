import asyncio


class Loop:
    def __init__(self):
        asyncio.set_event_loop(asyncio.new_event_loop())
        self.loop = asyncio.get_event_loop()

    def run_until_complete(self, async_func):
        self.loop.run_until_complete(async_func())
        self.loop.close()
