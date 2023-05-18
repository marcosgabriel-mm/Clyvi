from .usuario import Usuario


class Artista(Usuario):
    def __init__(
        self, nome, data_de_nascimento, idade, e_mail, senha, quantidade_de_musicas
    ) -> None:
        super().__init__(nome, data_de_nascimento, idade, e_mail, senha)
        self.quantidade_de_musicas = quantidade_de_musicas

    def __str__(self) -> str:
        return super().__str__()

    
    def entrar_na_conta_artista():
        pass