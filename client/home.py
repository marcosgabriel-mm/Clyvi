from server.models.busca import Busca
from server.models.musica import Musica

#Por meio do Singleton, certifico que há apenas uma instância       
busca = Busca.instance()

def informacoes_conta(user):
    try:
        print(f"Nome: {user['nome']}\nIdade: {user['idade']}\nData de Nascimento: {user['data_de_nascimento']}\nEmail: {user['e-mail']}\n")
    except TypeError:
        print(f"Nome: {user.nome}\nIdade: {user.idade}\nData de Nascimento: {user.data_de_nascimento}\nEmail: {user.e_mail}\n")


def opcoes_dentro_do_sistema(usuario=None):
    while True:
        opcao = int(input("\n[1] - Escutar uma Musica\n[2] - Publicar uma música\n[3] - Buscar\n[4] - Conta\n[5] - Artista Cadastrados\n[6] - Fechar\n=> "))
        #user = Usuario.informacoes_da_conta(usuario)
        opcoes = {
            1: lambda: Musica.escutar_musicas(usuario),
            2: lambda: busca.publicar_musica(usuario),
            3: busca.procurar_artistas_musica,
            4: lambda: informacoes_conta(usuario),
            5: busca.listar_artistas_cadastrados,
            6: exit
        }
        
        acao = opcoes.get(opcao, lambda: print("Opção Invalida\n"))
        acao()
