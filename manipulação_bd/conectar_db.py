from pymongo import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://marcosgabriel:mgmm4103@cluster0.7mnfxzs.mongodb.net/?retryWrites=true&w=majority"

def conectar_ao_banco_de_dados():
    cliente = MongoClient(uri, server_api=ServerApi('1'))

    banco_de_dados = cliente['ClyviDB']
    colecao = banco_de_dados['usuarios']

    try:
        cliente.admin.command('ping')
        print("Conectado ao MongoDB!")
    except Exception as e:
        print(e)

    return colecao


