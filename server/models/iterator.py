from abc import ABCMeta, abstractmethod

class IIterator(metaclass=ABCMeta):
    "Interface do Iterator"
    @staticmethod
    @abstractmethod
    def has_next():
        "Retorna um valor booleano se é ou nao o fim da coleção"

    @staticmethod
    @abstractmethod
    def next():
        "Retorna um objeto na coleçãp"

class Iterable(IIterator):
    "O Iterator concreto"

    def __init__(self, aggregates):
        self.index = 0
        self.aggregates = aggregates

    def next(self):
        if self.index < len(self.aggregates):
            aggregate = self.aggregates[self.index]
            self.index += 1
            return aggregate
        raise Exception("AtEndOfIteratorException", "At End of Iterator")

    def has_next(self):
        return self.index < len(self.aggregates)