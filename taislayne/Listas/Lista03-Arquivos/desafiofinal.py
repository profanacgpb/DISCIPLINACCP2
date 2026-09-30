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

arquivo = open("produtos.txt", "w")

arquivo.write(produto1["nome"] + ";" + str(produto1["preco"]) + ";" + str(produto1["quantidade"]) + "\n")
arquivo.write(produto2["nome"] + ";" + str(produto2["preco"]) + ";" + str(produto2["quantidade"]) + "\n")
arquivo.write(produto3["nome"] + ";" + str(produto3["preco"]) + ";" + str(produto3["quantidade"]) + "\n")

arquivo.close()

arquivo = open("produtos.txt", "r")

for linha in arquivo:
    dados = linha.strip().split(";")

    nome = dados[0]
    preco = dados[1]
    quantidade = dados[2]

    print("Produto:", nome)
    print("Preço:", preco)
    print("Quantidade:", quantidade)
    print()

arquivo.close()