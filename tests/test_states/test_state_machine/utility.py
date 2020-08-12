from src.states.istate import IState


class MState(IState):
    def __init__(self, mocker):
        mocker.patch.object(self, 'next')
        mocker.patch.object(self, 'run')

    def run(self): pass
    def next(self): pass


def make_final_mock_state(mocker):
    result = MState(mocker)
    result.next.return_value = None
    return result


def make_initial_and_final_mock_states(mocker):
    initial = MState(mocker)

    final = make_final_mock_state(mocker)
    initial.next.return_value = final

    return initial, final
