produtos = {
    "Notebook": 2500,
    "Mouse": 80,
    "Teclado": 150,
    "Monitor": 900,
    "Headset": 200
}

# a) Mostrar todos os produtos
print("Todos os produtos:")

for produto in produtos:
    print(produto)

# b) Mostrar todos os preços
print("\nTodos os preços:")

for preco in produtos.values():
    print(preco)

# c) Mostrar produto e preço
print("\nProdutos e preços:")

for produto, preco in produtos.items():
    print(produto, ":", preco)

# d) Mostrar o produto mais caro
produto_caro = max(produtos, key=produtos.get)

print("\nProduto mais caro:")
print(produto_caro)
print("Preço:", produtos[produto_caro])