# DESAFIO FINAL - DICIONÁRIO + ARQUIVO

produtos = []

produto1 = {
    "nome": "Notebook",
    "preco": 2500,
    "quantidade": 5
}

produto2 = {
    "nome": "Mouse",
    "preco": 50,
    "quantidade": 20
}

produto3 = {
    "nome": "Teclado",
    "preco": 100,
    "quantidade": 10
}

produtos.append(produto1)
produtos.append(produto2)
produtos.append(produto3)

with open("produtos.txt", "w", encoding="utf-8") as arquivo:
    for produto in produtos:
        arquivo.write(produto["nome"] + ";" + str(produto["preco"]) + ";" + str(produto["quantidade"]) + "\n")

with open("produtos.txt", "r", encoding="utf-8") as arquivo:
    for linha in arquivo:
        dados = linha.strip().split(";")

        print("Produto:", dados[0])
        print("Preço:", dados[1])
        print("Quantidade:", dados[2])
        print("----------------")