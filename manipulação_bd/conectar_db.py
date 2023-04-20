from pymongo import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://marcosgabriel:mgmm4103@cluster0.7mnfxzs.mongodb.net/?retryWrites=true&w=majority"

class Banco:
    def __init__(self):
        self.cliente = MongoClient("mongodb+srv://marcosgabriel:mgmm4103@cluster0.7mnfxzs.mongodb.net/?retryWrites=true&w=majority", server_api=ServerApi('1'))
    def usuarios(self):
        banco_de_dados = self.cliente['ClyviDB']
        colecao = banco_de_dados['usuarios']
        return colecao
    def testar_conn(self):
        try:
            self.cliente.admin.command('ping')
            print("Conectado ao MongoDB!")
        except Exception as e:
            print(e)



