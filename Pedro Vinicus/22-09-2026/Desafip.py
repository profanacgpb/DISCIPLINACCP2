# DESAFIO FINAL - DICIONÁRIO + ARQUIVO

# Criando os produtos
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


# Criando o arquivo produtos.txt
arquivo = open("produtos.txt", "w")


# Gravando produto 1
arquivo.write(
    produto1["nome"] + ";" +
    str(produto1["preco"]) + ";" +
    str(produto1["quantidade"]) + "\n"
)


# Gravando produto 2
arquivo.write(
    produto2["nome"] + ";" +
    str(produto2["preco"]) + ";" +
    str(produto2["quantidade"]) + "\n"
)


# Gravando produto 3
arquivo.write(
    produto3["nome"] + ";" +
    str(produto3["preco"]) + ";" +
    str(produto3["quantidade"]) + "\n"
)


arquivo.close()


# Lendo o arquivo
arquivo = open("produtos.txt", "r")


for linha in arquivo:

    nome, preco, quantidade = linha.strip().split(";")

    print("Produto:", nome)
    print("Preço: R$", preco)
    print("Quantidade:", quantidade)
    print("------------------------")


arquivo.close()