from manipulação_bd.conectar_db import Banco
from src.dados_do_usuario import dados_usuario

class Usuario:
    def __init__(self, nome, data_de_nascimento, idade, e_mail, senha) -> None:
        self.nome = nome
        self.idade = idade
        self.data_de_nascimento = data_de_nascimento
        self.e_mail = e_mail
        self.__senha = senha
        self.playlists = {}

    def __str__(self) -> str:
        return f"Nome: {self.nome}\tIdade: {self.__idade}\tData de Nascimento: {self.__data_de_nascimento}\n\nEmail: {self.__e_mail}\nSenha : ******\n\n"

    @staticmethod
    def informacoes_da_conta():

        if "usuario_logado" in dados_usuario:
            usuario = dados_usuario["usuario_logado"]
            #print(usuario)
            return print(
                
                f"\nNome: {usuario.nome}\n"
                f"Idade: {usuario.idade}\n"
                f"E-mail: {usuario.e_mail}\n"
                f"Data de nascimento: {usuario.data_de_nascimento}"
            )        
        
    
    def criar_playlist(self, nome):
        if nome not in self.playlists:
            self.playlists[nome] = []

    def adicionar_musica_na_playlist(self, nome_playlist, musica):
        if nome_playlist in self.playlists:
            self.playlists[nome_playlist].append(musica)
        else:
            print("Playlist não encontrada.")

    def remover_musica_da_playlist(self, nome_playlist, musica):
        if nome_playlist in self.playlists:
            if musica in self.playlists[nome_playlist]:
                self.playlists[nome_playlist].remove(musica)
            else:
                print("Música não encontrada na playlist.")
        else:
            print("Playlist não encontrada.")

    def renomear_playlist(self, nome_antigo, nome_novo):
        if nome_antigo in self.playlists:
            self.playlists[nome_novo] = self.playlists.pop(nome_antigo)
        else:
            print("Playlist não encontrada.")

    def excluir_playlist(self, nome):
        if nome in self.playlists:
            del self.playlists[nome]
        else:
            print("Playlist não encontrada.")

    def exibir_playlists(self):
        if self.playlists:
            print("Playlists:")
            for nome, musicas in self.playlists.items():
                print(f"- {nome}: {len(musicas)} músicas")
        else:
            print("Nenhuma playlist encontrada.")
        