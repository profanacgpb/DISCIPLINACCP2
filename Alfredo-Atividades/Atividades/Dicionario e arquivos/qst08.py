produtos = {
    "Notebook": 3500,
    "Mouse": 80,
    "Teclado": 150,
    "Monitor": 900,
    "Headset": 250
}

print("Produtos:", list(produtos.keys()))

print("Preços:", list(produtos.values()))

print("\nProduto e preço:")
for produto, preco in produtos.items():
    print(f"{produto}: R$ {preco}")

mais_caro = max(produtos, key=produtos.get)
print(f"\nProduto mais caro: {mais_caro} R${produtos[mais_caro]}")