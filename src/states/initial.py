from src.states.istate import AState


class Initial(AState):
    async def call_actions(self):
        await self._state_actions.get_current_month_and_solve_captcha()
