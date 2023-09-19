import abc


class CreateFigureException(Exception):
    pass


class Figure(abc.ABC):
    @abc.abstractmethod
    def area(self) -> float:
        pass
