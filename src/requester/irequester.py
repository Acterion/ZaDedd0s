import abc

class IRequster(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def get_current_month(self):
        pass    
    
    @abc.abstractmethod
    def get_next_month(self):
        pass    