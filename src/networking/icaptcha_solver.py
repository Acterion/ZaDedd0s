import abc


class ICaptchaSolver(abc.ABC):
    @abc.abstractmethod
    def solve(self, base64_captcha):
        pass
