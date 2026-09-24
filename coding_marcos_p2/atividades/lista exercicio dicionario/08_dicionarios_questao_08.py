produtos = {
    "Notebook": 2500,
    "Mouse": 50,
    "Teclado": 100,
    "Monitor": 900,
    "Headset": 200
}

for produto in produtos.keys():
    print(produto)

for preco in produtos.values():
    print(preco)

for produto, preco in produtos.items():
    print(produto, "-", preco)

produto_mais_caro = max(produtos, key=produtos.get)
print(produto_mais_caro, "-", produtos[produto_mais_caro])
