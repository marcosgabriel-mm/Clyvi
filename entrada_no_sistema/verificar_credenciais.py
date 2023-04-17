import os, json,sys
sys.path.append('D:/VisualProjects/Music_system/src/models')

from src.models import usuario, artista
projeto_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
caminho_json = os.path.join(projeto_dir, 'json', 'banco_de_dados.json')

def verificar_login(e_mail, senha):
    with open (caminho_json, "r") as arq_json:
        dados = json.load(arq_json) 

    for campos in dados:
        print(campos["e_mail"])
        if campos["e_mail"] == e_mail and campos["senha"] == senha:
            '''if campos["tipo_de_conta"] == "usuario":
                associaUsuario = usuario.Usuario(campos["nome"],campos["data_de_nascimento"],campos["idade"],campos["e_mail"], campos["senha"])
            else:
                associaArtista = artista.Artista(campos["nome"],campos["data_de_nascimento"],campos["idade"],campos["e_mail"], campos["senha"],campos["total_de_musicas"])'''
            return 1
    return 0

def verificar_criacao_de_conta():
    pass