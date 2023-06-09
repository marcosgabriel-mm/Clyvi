from pymongo import MongoClient
from pymongo.server_api import ServerApi



class Banco:

    #Singleton Design Pattern
    _instance = None
    @classmethod
    def instance(cls):
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance

    def __init__(self):
        self.cliente = MongoClient(
            "mongodb+srv://marcosgabriel:mgmm4103@cluster0.7mnfxzs.mongodb.net/?retryWrites=true&w=majority",
            server_api=ServerApi("1"),
        )

    # Essa função provavelmente vai servir de muita coisa, já que retorna todos os usuários
    def busca_usuario(self, credenciais):
        banco_de_dados = self.cliente['ClivyDB']
        colecao = banco_de_dados['usuarios']
        return colecao.find_one(credenciais)
    
    def usuarios(self):
        banco_de_dados = self.cliente["ClyviDB"]
        colecao = banco_de_dados["usuarios"]
        return colecao.find()

    def inserir_usuarios(self, *args):
        banco_de_dados = self.cliente["ClyviDB"]
        colecao = banco_de_dados["usuarios"]
        colecao.insert_one(*args)
        return colecao.find_one(*args)

    def verificar_user_existente(self, *args):
        banco_de_dados = self.cliente["ClyviDB"]
        colecao = banco_de_dados["usuarios"]
        email = args[0]["e-mail"]
        resultado = colecao.find_one({"e-mail": email})
        if resultado == None:
            return True
        else:
            return False

    def verificar_credenciais(self, *args):
        banco_de_dados = self.cliente["ClyviDB"]
        colecao = banco_de_dados["usuarios"]
        #print(args)
        #print(*args)
        email = args[0]
        senha = args[1]
        resultado = colecao.find_one({"e-mail": email, "senha": senha})

        if resultado == None:
            return False
        else:
            return resultado

    def testar_conn(self):
        try:
            self.cliente.admin.command("ping")
            print("Conectado ao MongoDB!")
        except Exception as e:
            print(e)

    #Musicas

    def buscar_musicas(self):
        banco_de_dados = self.cliente["ClyviDB"]
        colecao = banco_de_dados["musicas"]
        return colecao.find()
