# Desafio final - Dicionário + Arquivo

produtos = [
    {"nome": "Notebook", "preco": 2500, "quantidade": 5},
    {"nome": "Mouse", "preco": 50, "quantidade": 20},
    {"nome": "Teclado", "preco": 100, "quantidade": 10},
]

with open("produtos.txt", "w") as arquivo:
    for produto in produtos:
        arquivo.write(f"{produto['nome']};{produto['preco']};{produto['quantidade']}\n")

with open("produtos.txt", "r") as arquivo:
    for linha in arquivo:
        nome, preco, quantidade = linha.strip().split(";")
        print(f"Produto: {nome} | Preço: R${preco} | Quantidade: {quantidade}")
