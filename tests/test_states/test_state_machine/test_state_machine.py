import src.states.state_mashine as sm
import tests.test_states.test_state_machine.utility as uti


def test_basic_work(mocker):
    initial, final = uti.make_initial_and_final_mock_states(mocker)
    machine = sm.StateMachine(initial)
    machine.exec()
    final.run.assert_called_once()
