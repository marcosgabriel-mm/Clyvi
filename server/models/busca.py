from server.conectar_db import Banco
from server.models.iterator import Iterable
from server.models.musica import Musica

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