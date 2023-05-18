from manipulação_bd.conectar_db import Banco
from src.models.usuario import Usuario
from src.models.artista import Artista
from datetime import datetime
from src.dados_do_usuario import dados_usuario

def calcular_idade_a_partir_da_data_de_nascimento(data_de_nascimento):
  
    data_atual = datetime.now()
    data_de_nascimento = datetime.strptime(data_de_nascimento, "%d/%m/%Y")
    idade = data_atual.year - data_de_nascimento.year

    if data_atual.month < data_de_nascimento.month or (data_atual.month == data_de_nascimento.month and data_atual.day < data_de_nascimento.day):
        idade -= 1
    
    return idade

def login_no_sistema():

    banco = Banco()

    while True:
        e_mail = input("Digite seu E-mail: ")
        senha = input("Digite sua Senha: ")

        conta_valida, documento_resgatado = banco.verificar_credenciais(e_mail, senha)

        # verifica se o login está certo
        if conta_valida:
            print("\nBem Vindo de Volta\n")
            if documento_resgatado["tipo_de_conta"] == "usuario":
                usuario_logado = Usuario(documento_resgatado["nome"],documento_resgatado["data_de_nascimento"],documento_resgatado["idade"], documento_resgatado["e-mail"], documento_resgatado["senha"])
                dados_usuario["usuario_logado"] = usuario_logado
            else:
                usuario_logado = Artista(documento_resgatado["nome"],documento_resgatado["data_de_nascimento"],documento_resgatado["idade"], documento_resgatado["e-mail"], documento_resgatado["senha"],documento_resgatado["quantidade_de_musicas"])
                dados_usuario["usuario_logado"] = usuario_logado
                #carregar lista de musicas
            return False
        else:
            print("\nE-Mail ou Senha errado\nDigite Novamente\n\n")


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
        "idade": calcular_idade_a_partir_da_data_de_nascimento(data_de_nascimento)
    }

    banco = Banco()

    if (banco.verificar_user_existente(credenciais)) == True:
        credenciais["tipo_de_conta"] = "usuario"
        banco.inserir_usuarios(credenciais)

        Usuario(nome,data_de_nascimento,calcular_idade_a_partir_da_data_de_nascimento(data_de_nascimento),e_mail,senha)

    else:
        print("Já existe uma conta com esse email. Considere fazer login")

# opções que podem ser escolhidas de inicio
opcoes = {1: login_no_sistema, 2: criar_conta}


def opcoes_na_entrada_do_sistema():
    opcao = int(input("\tBem Vindo\t\n[1] - Entrar\n[2] - Criar Conta\n\n=> "))

    acao = opcoes.get(opcao, lambda: print("Opção Invalida\n"))
    acao()

    return True
