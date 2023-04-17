

class Usuario:

    def __init__(self, nome, data_de_nascimento, idade, e_mail, senha) -> None:
        self.nome  = nome
        self.__idade = idade
        self.__data_de_nascimento = data_de_nascimento
        self.__e_mail = e_mail
        self.__senha = senha

    def __str__(self) -> str:
        return f"Nome: {self.nome}\tIdade: {self.__idade}\tData de Nascimento: {self.__data_de_nascimento}\n\nEmail: {self.__e_mail}\nSenha : ******\n\n"
    