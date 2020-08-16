from src.states.initial import Initial
from src.states.ddosing import Ddosing
from src.states.penetration import Penetration
from src.states.final_states import Error, Success


class StatesFactory:
    def __init__(self, state_actions):
        self._state_actions = state_actions
        self._error_state = self._make_error()

    def make_initial(self, ddosing=None) -> Initial:
        ddosing = self.make_ddosing() if ddosing is None else ddosing
        return Initial(self._state_actions, {'ddosing': ddosing}, self._error_state)

    def make_ddosing(self, penetration=None) -> Ddosing:
        result = Ddosing(self._state_actions, None, self._error_state)

        if penetration is None:
            penetration = self._make_penetration(self.make_success(), result)

        result.set_next_states({'penetration': penetration})
        return result

    def make_penetration(self, success=None, ddosing=None) -> Penetration:
        result = Penetration(self._state_actions, None, self._error_state)

        success = self.make_success() if success is None else success
        ddosing = self.make_ddosing(result) if ddosing is None else ddosing

        result.set_next_states({'success': success, 'ddosing': ddosing})

        return result

    def make_success(self) -> Success:
        return Success(self._state_actions, 'Success!')

    def _make_error(self):
        return Error(self._state_actions)

    def _make_penetration(self, success, ddosing):
        return Penetration(self._state_actions, {'success': success, 'ddosing': ddosing}, self._error_state)

    def _make_ddosing(self, penetration):
        return Ddosing(self._state_actions, penetration, self._error_state)
