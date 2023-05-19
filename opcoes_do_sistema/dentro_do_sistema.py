from src.models.musica import Musica
from manipulação_bd.conectar_db import Banco
from src.models.usuario import Usuario
from opcoes_do_sistema.entrando_no_sistema import opcoes_na_entrada_do_sistema


class Busca(Banco):

    def procurar_artistas(self):
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
def publicar_musica():
    pass

busca = Busca()
opcoes = {
    1: Musica.escutar_musicas,
    2: Usuario.criar_playlist,
    3: busca.procurar_artistas,
    4: Usuario.informacoes_da_conta,
    5: opcoes_na_entrada_do_sistema
}

def opcoes_dentro_do_sistema():
    opcao = int(input("\n[1] - Escutar uma Musica\n[2] - Criar Playlist\n[3] - Buscar\n[4] - Conta\n\n=> "))

    acao = opcoes.get(opcao, lambda: print("Opção Invalida\n"))
    acao()
