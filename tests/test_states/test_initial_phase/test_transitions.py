from src.states.states_factory import StatesFactory
from src.states.state_machine import StateMachine
from tests.test_states.test_initial_phase.utility import FakeStateActions, FakeError

import tests.test_states.utility as uti


def test_initial_to_ddosing():
    actions = FakeStateActions()
    factory = StatesFactory(actions, FakeError())
    ddosing_sate = uti.FFinalState()
    fsm = StateMachine(factory.make_initial(ddosing_sate))

    fsm.exec()

    assert actions.get_current_month_and_solve_captcha_was_called_once
    ddosing_sate.assert_run_was_called()


def test_initial_to_error():
    error_sate = FakeError()
    factory = StatesFactory(FakeStateActions(network_error=True), error_sate)
    fsm = StateMachine(factory.make_initial())

    fsm.exec()

    error_sate.assert_finalize_was_called()


def test_ddosing_to_penetration_through_current_month():
    actions = FakeStateActions(free_places_in_current_month=True)
    factory = StatesFactory(actions, FakeError())
    penetration = uti.FFinalState()
    fsm = StateMachine(factory.make_ddosing(penetration))

    fsm.exec()

    assert actions.check_free_places_in_current_month_was_called_once
    penetration.assert_run_was_called()


def test_ddosing_to_penetration_through_next_month():
    actions = FakeStateActions(free_places_in_next_month=True)
    factory = StatesFactory(actions, FakeError())
    penetration = uti.FFinalState()
    fsm = StateMachine(factory.make_ddosing(penetration))

    fsm.exec()

    assert actions.check_free_places_in_next_month_was_called_once
    penetration.assert_run_was_called()


def test_penetration_to_ddosing():
    actions = FakeStateActions(place_reserved=False)
    factory = StatesFactory(actions, FakeError())
    ddosing = uti.FFinalState()
    fsm = StateMachine(factory.make_penetration(ddosing=ddosing))

    fsm.exec()

    assert actions.try_to_reserve_place_was_called_once
    ddosing.assert_run_was_called()


def test_penetration_to_success():
    actions = FakeStateActions(place_reserved=True)
    factory = StatesFactory(actions, FakeError())
    success = uti.FFinalState()
    fsm = StateMachine(factory.make_penetration(success=success))

    fsm.exec()

    assert actions.try_to_reserve_place_was_called_once
    success.assert_run_was_called()
