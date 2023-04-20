# importa os para arquivos, json para o arquivo json, e sys para path
import os, json

# faço a minima ideia, mas é para chegar no diretorio do aquivo banco_de_dados.json
projeto_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
caminho_json = os.path.join(projeto_dir, "json", "banco_de_dados.json")


def verificar_login(e_mail, senha):
    # abre o arquivo em modo de leitura
    with open(caminho_json, "r") as arq_json:
        # carrega os dados do aquivo para a variavel
        dados = json.load(arq_json)

    # laço em toda a variavel
    for campos in dados:
        # print(campos["e_mail"])
        # caso email e senha correta "tudo certo", se não, ja sabe
        if campos["e_mail"] == e_mail and campos["senha"] == senha:
            """if campos["tipo_de_conta"] == "usuario":
                associaUsuario = usuario.Usuario(campos["nome"],campos["data_de_nascimento"],campos["idade"],campos["e_mail"], campos["senha"])
            else:
                associaArtista = artista.Artista(campos["nome"],campos["data_de_nascimento"],campos["idade"],campos["e_mail"], campos["senha"],campos["total_de_musicas"])
            """
            return 1
    return 0


# TODO fazer a criação de conta, no caso verificar se ja existe email cadastrado
def verificar_criacao_de_conta():
    pass
