import abc


class Executions(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def run(self):
        pass
