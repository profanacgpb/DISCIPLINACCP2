produtos = [
    {"nome": "Notebook", "preco": 2500, "quantidade": 5},
    {"nome": "Mouse", "preco": 50, "quantidade": 20},
    {"nome": "Teclado", "preco": 100, "quantidade": 10}
]

with open("produtos.txt", "w") as arquivo:
    for produto in produtos:
        linha = (
            produto["nome"] + ";" +
            str(produto["preco"]) + ";" +
            str(produto["quantidade"]) + "\n"
        )
        arquivo.write(linha)

with open("produtos.txt", "r") as arquivo:
    for linha in arquivo:
        dados = linha.strip().split(";")
        nome = dados[0]
        preco = dados[1]
        quantidade = dados[2]

        print("Produto:", nome)
        print("Preço:", preco)
        print("Quantidade:", quantidade)
