from server.conectar_db import Banco

class Busca(Banco):

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
def publicar_musica():
    pass

busca = Busca()

def informacoes_conta(user):
    try:
        print(f"Nome: {user['nome']}\nIdade: {user['idade']}\nData de Nascimento: {user['data_de_nascimento']}\nEmail: {user['e-mail']}\n")
    except TypeError:
        print(f"Nome: {user.nome}\nIdade: {user.idade}\nData de Nascimento: {user.data_de_nascimento}\nEmail: {user.e_mail}\n")


def opcoes_dentro_do_sistema(usuario=None):
    opcao = int(input("\n[1] - Escutar uma Musica\n[2] - Criar Playlist\n[3] - Buscar\n[4] - Conta\n\n=> "))
    #user = Usuario.informacoes_da_conta(usuario)
    opcoes = {
        #1: Musica.escutar_musicas(usuario),
        2: publicar_musica,
        3: busca.procurar_artistas_musica,
        4: lambda: informacoes_conta(usuario),

    }
    
    acao = opcoes.get(opcao, lambda: print("Opção Invalida\n"))
    acao()