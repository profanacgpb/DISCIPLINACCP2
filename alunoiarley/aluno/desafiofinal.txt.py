produto = {
    "nome": "Notebook",
    "preco": 2500,
    "quantidade": 5
}
with open("produtos.txt", "w", encoding="utf-8") as arquivo:
    arquivo.write(
        f"{produto['nome']};{produto['preco']};{produto['quantidade']}\n"
    )
with open("produtos.txt", "r", encoding="utf-8") as arquivo:
    for linha in arquivo:
        nome, preco, quantidade = linha.strip().split(";")

        print("Produto:", nome)
        print("Preço: R$", preco)
        print("Quantidade:", quantidade)
        print("-" * 30)