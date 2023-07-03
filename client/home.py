from server.conectar_db import Banco
from src.models.musica import Musica
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

class Busca(Banco):
    #Singleton Design Pattern
    _instance = None
    @classmethod
    def instance(cls):
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance
    
    def listar_artistas_cadastrados(self):
        banco_de_dados = self.cliente["ClyviDB"]
        colecao = banco_de_dados["usuarios"]
        file = list(colecao.find({'tipo_de_conta': "artista"}))
        
        iteravel = Iterable(file)
        while iteravel.has_next():
            print(iteravel.next()['nome'])

    def procurar_artistas_musica(self):
        banco_de_dados = self.cliente["ClyviDB"]
        colecao = banco_de_dados["usuarios"]
        query = {"nome": "Vex", "tipo_de_conta":"artista"}
        resultados = colecao.find(query)
        
        print("----------------------")
        print("Artistas: ")
        
        for artista in resultados:
            print(artista)
        
        print("----------------------")
        print("Músicas: ")
        
        colecao = banco_de_dados["musicas"]
        query = {"nome": "Vex"}
        resultados = colecao.find(query)
        
        for musica in resultados:
            print(f"{musica['nome']} - {musica['artista']}")

    #usuario publica e sua conta passa de usuario para artista,
    def publicar_musica(self, usuario):
        banco_de_dados = self.cliente["ClyviDB"]
        colecao = banco_de_dados["usuarios"]

        colecao.update_one({'_id': usuario['_id']}, {'$set': {'tipo_de_conta': 'artista'}})

        musica = Musica(usuario)
        musica_dict = musica.gerar_dicionario()
        
        musicas_colecao = banco_de_dados['musicas']
        musicas_colecao.insert_one(musica_dict)

#Por meio do Singleton, certifico que há apenas uma instância       
busca = Busca.instance()

def informacoes_conta(user):
    try:
        print(f"Nome: {user['nome']}\nIdade: {user['idade']}\nData de Nascimento: {user['data_de_nascimento']}\nEmail: {user['e-mail']}\n")
    except TypeError:
        print(f"Nome: {user.nome}\nIdade: {user.idade}\nData de Nascimento: {user.data_de_nascimento}\nEmail: {user.e_mail}\n")


def opcoes_dentro_do_sistema(usuario=None):
    while True:
        opcao = int(input("\n[1] - Escutar uma Musica\n[2] - Publicar uma música\n[3] - Buscar\n[4] - Conta\n[5] - Artista Cadastrados\n=> "))
        #user = Usuario.informacoes_da_conta(usuario)
        opcoes = {
            1: lambda: Musica.escutar_musicas(usuario),
            2: lambda: busca.publicar_musica(usuario),
            3: busca.procurar_artistas_musica,
            4: lambda: informacoes_conta(usuario),
            5: busca.listar_artistas_cadastrados

        }
        
        acao = opcoes.get(opcao, lambda: print("Opção Invalida\n"))
        acao()
