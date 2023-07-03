from server.conectar_db import Banco
from server.models.usuario import Usuario
from client.home import opcoes_dentro_do_sistema

def login_no_sistema():

    banco = Banco()

    while True:
        e_mail = input("Digite seu E-mail: ")
        senha = input("Digite sua Senha: ")

        documento_resgatado = banco.verificar_credenciais(e_mail, senha)

        # verifica se o login está certo
        if documento_resgatado!=False:
            print("\nBem Vindo de Volta\n")
            if  documento_resgatado["tipo_de_conta"] == ("usuario"):

                opcoes_dentro_do_sistema(documento_resgatado)
                
                # usuario_logado = Usuario(documento_resgatado["nome"],documento_resgatado["data_de_nascimento"],documento_resgatado["idade"], documento_resgatado["e-mail"], documento_resgatado["senha"])
                # dados_usuario["usuario_logado"] = usuario_logado
            else:

                opcoes_dentro_do_sistema(documento_resgatado)


                # usuario_logado = Artista(documento_resgatado["nome"],documento_resgatado["data_de_nascimento"],documento_resgatado["idade"], documento_resgatado["e-mail"], documento_resgatado["senha"],documento_resgatado["quantidade_de_musicas"])
                # dados_usuario["usuario_logado"] = usuario_logado
                #carregar lista de musicas
        else:
            print("\nE-Mail ou Senha errado\nDigite Novamente\n\n")


def criar_conta():


    banco = Banco()
    usuario_novo = Usuario()

    credenciais = usuario_novo.credenciais

    if (banco.verificar_user_existente(credenciais)) == True:
        credenciais["tipo_de_conta"] = "usuario"
        documento = banco.inserir_usuarios(credenciais)
        
        print ("\nConta criada com sucesso")
        opcoes_dentro_do_sistema(documento)
        
        # usuario_logado = Usuario(nome,data_de_nascimento,calcular_idade_a_partir_da_data_de_nascimento(data_de_nascimento),e_mail,senha)
        # dados_usuario["usuario_logado"] = usuario_logado
    else:
        print("\nJá existe uma conta com esse email. Considere fazer login")

# opções que podem ser escolhidas de inicio
opcoes = {1: login_no_sistema, 2: criar_conta, 3: exit}


def opcoes_na_entrada_do_sistema():
    opcao = int(input("\tBem Vindo\t\n[1] - Entrar\n[2] - Criar Conta\n[3] - Fechar\n=> "))

    acao = opcoes.get(opcao, lambda: print("Opção Invalida\n"))
    acao()

    return True
