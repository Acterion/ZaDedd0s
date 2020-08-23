import abc


class IStateActionsFactory(abc.ABC):
    @abc.abstractmethod
    def make_sate_actions(self):
        pass
