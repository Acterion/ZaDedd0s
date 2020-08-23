from tests.test_states.test_transitions.fixtures \
    import fsm_and_ddosing_boys, fsm_and_failing_boys, \
    fsm_and_penetrating_this_month_boys, fsm_and_penetrating_next_month_boys, \
    fsm_and_failed_penetration_boys, fsm_and_penetrated_boys


def test_initial_to_ddosing(fsm_and_ddosing_boys):
    fsm_and_ddosing_boys.fsm.start()

    assert fsm_and_ddosing_boys.actions.get_current_month_and_solve_captcha_was_called_once
    assert fsm_and_ddosing_boys.ddosing.run_was_called


def test_initial_to_error(fsm_and_failing_boys):
    fsm_and_failing_boys.fsm.start()

    assert fsm_and_failing_boys.actions.notify_subscribers_was_called_with == 'Error: 404'


def test_ddosing_to_penetration_through_current_month(fsm_and_penetrating_this_month_boys):
    fsm_and_penetrating_this_month_boys.fsm.start()

    assert fsm_and_penetrating_this_month_boys.actions.check_free_places_in_current_month_was_called_once
    assert fsm_and_penetrating_this_month_boys.penetration.run_was_called


def test_ddosing_to_penetration_through_next_month(fsm_and_penetrating_next_month_boys):
    fsm_and_penetrating_next_month_boys.fsm.start()

    assert fsm_and_penetrating_next_month_boys.actions.check_free_places_in_next_month_was_called_once
    assert fsm_and_penetrating_next_month_boys.penetration.run_was_called


def test_penetration_to_ddosing(fsm_and_failed_penetration_boys):
    fsm_and_failed_penetration_boys.fsm.start()

    assert fsm_and_failed_penetration_boys.actions.try_to_reserve_place_was_called_once
    assert fsm_and_failed_penetration_boys.ddosing.run_was_called


def test_penetration_to_success(fsm_and_penetrated_boys):
    fsm_and_penetrated_boys.fsm.start()

    assert fsm_and_penetrated_boys.actions.try_to_reserve_place_was_called_once
    assert fsm_and_penetrated_boys.actions.notify_subscribers_was_called_with == 'Success!'
