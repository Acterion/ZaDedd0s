import abc


class IState(abc.ABC):
    @abc.abstractmethod
    def run(self):
        pass

    @abc.abstractmethod
    def next(self):
        pass


class AErrorState(IState):
    async def run(self):
        self.finalize()

    def next(self):
        pass

    def finalize(self):
        pass
