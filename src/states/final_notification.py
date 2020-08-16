from src.states.istate import IState


class FinalNotification(IState):
    def __init__(self, state_actions, message=None):
        self._state_actions = state_actions
        self._message = message

    async def run(self):
        await self._state_actions.notify_subscribers(self._message)

    def next(self):
        pass

    def set_message(self, message: str):
        self._message = message
