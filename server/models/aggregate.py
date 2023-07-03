from abc import ABCMeta, abstractmethod

class IAggregate(metaclass=ABCMeta):
    "Interface do objeto"
    @staticmethod
    @abstractmethod
    def method():
        "Busca"

class Aggregate(IAggregate):
    "Objeto Concreto"
    @staticmethod
    def method():
        print("Listar Artistas")