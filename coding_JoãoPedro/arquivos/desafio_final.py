
produto = {
    "nome": "Notebook",
    "preco": 2500,
    "quantidade": 5
}


arquivo = open("produtos.txt", "w")

arquivo.write(
    produto["nome"] + ";" +
    str(produto["preco"]) + ";" +
    str(produto["quantidade"]) + "\n"
)

arquivo.write("Mouse;50;20\n")
arquivo.write("Teclado;100;10\n")

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

