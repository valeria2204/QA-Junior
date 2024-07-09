import abc


class Actions(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def run(self):
        pass
