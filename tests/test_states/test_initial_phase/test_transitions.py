from src.states.initial import Initial
from src.states.ddosing import Ddosing
from src.states.state_machine import StateMachine
from tests.test_states.test_initial_phase.utility import FakeStateActions, FakeError

import tests.test_states.utility as uti


def test_initial_to_ddosing():
    actions = FakeStateActions()
    ddosing_sate = uti.FFinalState()
    fsm = StateMachine(Initial(actions, ddosing_sate, None))

    fsm.exec()

    assert actions.get_current_month_and_solve_captcha_was_called_once
    ddosing_sate.assert_run_was_called()


def test_initial_to_error():
    error_sate = FakeError()
    fsm = StateMachine(Initial(FakeStateActions(network_error=True), uti.FFinalState(), error_sate))

    fsm.exec()

    error_sate.assert_finalize_was_called()


def test_ddosing_to_penetration_through_current_month():
    actions = FakeStateActions(free_places_in_current_month=True)
    penetration = uti.FFinalState()
    fsm = StateMachine(Ddosing(actions, penetration, None))

    fsm.exec()

    assert actions.check_free_places_in_current_month_was_called_once
    penetration.assert_run_was_called()


def test_ddosing_to_penetration_through_next_month():
    actions = FakeStateActions(free_places_in_next_month=True)
    penetration = uti.FFinalState()
    fsm = StateMachine(Ddosing(actions, penetration, None))

    fsm.exec()

    assert actions.check_free_places_in_next_month_was_called_once
    penetration.assert_run_was_called()
