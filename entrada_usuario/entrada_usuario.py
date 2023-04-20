from manipulação_bd.conectar_db import Banco


def login_no_sistema():

    banco = Banco()

    while 1:
        e_mail = input("Digite seu E-mail: ")
        senha = input("Digite sua Senha: ")

        # verifica se o login está certo
        if banco.verificar_credenciais(e_mail, senha) == True:
            print("\nBem Vindo de Volta\n")
            return 0
        else:
            print("\nE-Mail ou Senha errado\nDigite Novamente\n")


def criar_conta():
    nome = input("Digite seu nome: ")
    data_de_nascimento = input("Digite sua data de nascimento (D/M/A): ")
    e_mail = input("Digite seu E-Mail: ")  # verificar e-mail
    senha = input("Digite sua Senha: ")  # Colocar Minimos de Caracteres
    credenciais = {
        "nome": nome,
        "data_de_nascimento": data_de_nascimento,
        "e-mail": e_mail,
        "senha": senha,
    }

    banco = Banco()

    if (banco.verificar_user_existente(credenciais)) == True:
        banco.inserir_usuarios(credenciais)
    else:
        print("Já existe uma conta com esse email. Considere fazer login")

# opções que podem ser escolhidas de inicio
opcoes = {1: login_no_sistema, 2: criar_conta}


def escolher_opcoes():
    opcao = input("\tBem Vindo\t\n[1] - Entrar\n[2] - Criar Conta\n\n=> ")
    opcao = int(opcao)

    acao = opcoes.get(opcao, lambda: print("Opção Invalida\n"))
    acao()
