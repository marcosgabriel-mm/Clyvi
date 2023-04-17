from entrada_no_sistema.verificar_credenciais import verificar_login

def login_no_sistema():
   
    while(1):
        e_mail = input("Digite seu E-mail: ")
        senha = input("Digite sua Senha: ")

        if verificar_login(e_mail,senha):
            print("\nBem Vindo de Volta\n")
            return 0
        else:
            print("\nE-Mail ou Senha errado\nDigite Novamente\n")
            
    

def criar_conta():

    nome = input("Digite seu nome: ")
    data_de_nascimento = input("Digite sua data de nascimento (D/M/A): ")
    e_mail = input("Digite seu E-Mail: ") #verificar e-mail
    senha = input("Digite sua Senha: ") #Colocar Minimos de Caracteres

    credenciais = {nome, data_de_nascimento, e_mail, senha}
    return credenciais

opcoes = {
    1: login_no_sistema,
    2: criar_conta
}

def escolher_opcoes():

    opcao = input("\tBem Vindo\t\n[1] - Entrar\n[2] - Criar Conta\n\n=> ")
    opcao = int(opcao)

    acao = opcoes.get(opcao, lambda: print("Opção Invalida\n"))
    acao()
