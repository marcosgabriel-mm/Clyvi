
class Musica:

    def __init__(self, nome_da_musica, genero_musical, duracao_da_musica, artista_da_musica) -> None:
        self.nome_da_musica = nome_da_musica
        self.genero_musical = genero_musical
        self.duracao_da_musica = duracao_da_musica
        self.artista_da_musica = artista_da_musica

    def __str__(self) -> str:
        return f"Nome da Musica: {self.nome_da_musica}\nGênero da Musica: {self.genero_musical}\nDuração da Musica: {self.duracao_da_musica}\nArtista: {self.artista_da_musica}"
    
