def atualizar_documento(nome_da_colecao,nome):

    documento_procurado = nome_da_colecao.find(
        {"nome":nome}
    )

    for documento in documento_procurado:
        print(documento)