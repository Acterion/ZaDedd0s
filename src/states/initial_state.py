from src.states.istate import IState


class InitialError(IState):
    def __init__(self, requester):
        self.requester = requester

    def run(self):
        pass    
    
    def next(self):
        pass


class InitialCaptchaEntering(IState):
    def __init__(self, requester):
        self.requester = requester

    def run(self):
        pass
    
    def next(self):
        pass


class InitialState(IState):
    def __init__(self, requester):
        self.requester = requester
        self.error = ''

    def run(self):
        response = self.requester.get_current_month()
        if not response:
            self.error = response.error
        # check captcha presence??

    def next(self):
        if self.error:
            return InitialError(self.requester)
        return InitialCaptchaEntering(self.requester)
