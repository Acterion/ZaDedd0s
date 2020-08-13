import src.states.state_mashine as sm
import tests.test_states.test_state_machine.utility as uti


def test_async_run_in_state():
    initial, final = uti.make_initial_and_final_fake_states()
    machine = sm.StateMachine(initial)

    machine.exec()

    final.get_run_was_called()
