from server.conectar_db import Banco
from server.models.usuario import Usuario

import time, keyboard

class Musica:
    def __init__(
        self, nome_da_musica, genero_musical, duracao_da_musica, artista_da_musica
    ) -> None:
        self.nome_da_musica = nome_da_musica
        self.genero_musical = genero_musical
        self.duracao_da_musica = duracao_da_musica
        self.artista_da_musica = artista_da_musica
        self.tocando = False

    def __str__(self) -> str:
        return f"Nome da Musica: {self.nome_da_musica}\nGênero da Musica: {self.genero_musical}\nDuração da Musica: {self.duracao_da_musica}\nArtista: {self.artista_da_musica}"

    def pausar_musica(self):
        self.tocando = False

    def retomar_musica(self):
        self.tocando = True

    def passar_musica(self, playlist, index_atual):
        if index_atual < len(playlist) - 1:
            # Avança para a próxima música na lista
            proximo_index = index_atual + 1
            return playlist[proximo_index], proximo_index
        else:
            # Já está na última música da lista
            return None, index_atual
    
    def voltar_musica(self, playlist, index_atual):
        if index_atual > 0:
            # Retrocede para a música anterior na lista
            anterior_index = index_atual - 1
            return playlist[anterior_index], anterior_index
        else:
            # É a primeira música da lista, retorna a mesma música
            return playlist[index_atual], index_atual


    def escutar_musicas(usuario:Usuario=None):
        
        banco = Banco()
        playlist = list(banco.buscar_musicas())
        index_atual = 0

        while True:
            try:
                musica = playlist[index_atual]
                musica_obj = Musica(musica["nome"], musica["genero"], musica["duração"], musica["artista"])
                banco.adicionar_musica_historico(usuario, musica_obj)
                musica_obj.tocando = True

                print(f"\nTocando {musica_obj.nome_da_musica} - do Artista {musica_obj.artista_da_musica} ({musica_obj.genero_musical})")
                for i in range(musica_obj.duracao_da_musica):

                    if not musica_obj.tocando:
                        keyboard.wait(' ')
                        print("\nRetomando música.")
                        musica_obj.tocando = True 

                    else:
                        tempo_decorrido = f"{i}s".rjust(3, '0')
                        print(f"\rTempo decorrido: {tempo_decorrido}", end='', flush=True)
                        time.sleep(1)

                        if keyboard.is_pressed("space"):
                            print("\nMúsica pausada. Pressione 'espaço' para retomar.")
                            musica_obj.tocando = False

                    if keyboard.is_pressed("right"):
                        print("\nAvançando para a próxima música.")
                        musica_obj.pausar_musica()
                        proxima_musica, index_atual = musica_obj.passar_musica(playlist, index_atual)
                        if proxima_musica is not None:
                            break
                        else:
                            print("Não há mais músicas na playlist.")
                            return
                        
                    if keyboard.is_pressed("left"):         
                        print("\nVoltando para a música anterior.")
                        musica_obj.pausar_musica()
                        musica_anterior, index_atual = musica_obj.voltar_musica(playlist, index_atual)
                        if musica_anterior is not None:
                            break
                        else:
                            print("Essa é a primeira música da playlist.")
                            return

                    if keyboard.is_pressed("esc"):
                        return False

                print("\nAvançando para a próxima música.")
                proxima_musica, index_atual = musica_obj.passar_musica(playlist, index_atual)

            except StopIteration:
                print("Não há mais músicas na playlist.")
                return              