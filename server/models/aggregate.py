from abc import ABCMeta, abstractmethod

class IAggregate(metaclass=ABCMeta):
    "An interface that the aggregates should implement"
    @staticmethod
    @abstractmethod
    def method():
        "Método a ser implementado"

class Aggregate(IAggregate):
    "A concrete object"
    @staticmethod
    def method():
        print("Esse método foi chamado")