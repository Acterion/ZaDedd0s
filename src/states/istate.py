import abc


class IState(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def run(self):
        pass

    @abc.abstractmethod
    def next(self):
        pass
