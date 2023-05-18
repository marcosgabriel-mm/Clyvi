from src.models.musica import Musica
from manipulação_bd.conectar_db import Banco


class Busca():
    def __init__(self):
        #pensa no spotify quando procura uma musica ou artista
        banco = Banco()
    def procurar_artistas(self, input):
        pass
    def procurar_musicas(self, input):
        pass
    


#cria uma playlist com o nome que o usuario colocar
def criar_playlist():
    pass

#usuario publica e sua conta passa de usuario para artista,
def publicar_musica():
    pass

busca = Busca()
opcoes = {
    1: Musica.escutar_musicas,
    2: criar_playlist,
    3: busca.procurar_artistas,
    4: busca.procurar_musicas,
}

def opcoes_dentro_do_sistema():
    opcao = int(input("\n[1] - Escutar uma Musica\n[2] - Criar Playlist\n[3] - Buscar\n[4] - Conta\n\n=> "))

    acao = opcoes.get(opcao, lambda: print("Opção Invalida\n"))
    acao()
