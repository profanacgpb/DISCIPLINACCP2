produtos = {
    "Notebook": 2500,
    "Celular": 1500,
    "Tablet": 1200,
    "Teclado": 200,
    "Monitor": 900
}

print("Produtos:")
for produto in produtos:
    print(produto)

print("Preços:")
for preco in produtos.values():
    print(preco)

print("Produto e preço:")
for produto, preco in produtos.items():
    print(produto, preco)

mais_caro = max(produtos, key=produtos.get)

print("Produto mais caro:", mais_caro)