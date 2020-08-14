import abc


class IDdoser(abc.ABC):
    @abc.abstractmethod
    def get_current_month(self):
        pass    
    
    @abc.abstractmethod
    def get_next_month(self):
        pass
