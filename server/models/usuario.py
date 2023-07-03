from datetime import datetime

class Usuario:
    def __init__(self):
        
        self.nome = input("Digite seu nome: ")
        self.data_de_nascimento = input("Digite sua data de nascimento (D/M/A): ")
        self.e_mail = input("Digite seu E-Mail: ")
        self.senha = input("Digite sua Senha: ")  
        self.historico = []
        data_atual = datetime.now()
        self.data_de_nascimento = datetime.strptime(self.data_de_nascimento, "%d/%m/%Y")
        self.idade = data_atual.year - self.data_de_nascimento.year
        if data_atual.month < self.data_de_nascimento.month or (data_atual.month == self.data_de_nascimento.month and data_atual.day < self.data_de_nascimento.day):
            self.idade -= 1

        self.credenciais = {
        "nome": self.nome,
        "data_de_nascimento": self.data_de_nascimento,
        "e-mail": self.e_mail,
        "senha": self.senha,
        "idade": self.idade,
        "historico":self.historico
    }

    def informacoes_da_conta(self):
        return f"Nome: {self.nome}\tIdade: {self.idade}\tData de Nascimento: {self.data_de_nascimento}\n\nEmail: {self.e_mail}\n\n"     
    
    