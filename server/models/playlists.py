class Playlist(): 
    # def criar_playlist():
    #     nome = input("Nome da PlayList: ")

    #     usuario = Usuario
    #     if nome not in usuario.playlists:
    #         usuario.playlists[nome] = []

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
        