with open("compras.txt", "w", encoding="utf-8") as arquivo:
    print("Cadastre 5 produtos:")
    for i in range(1, 6):
        produto = input(f"Produto {i}: ")
        arquivo.write(produto + "\n")

print("\nLista de compras:")
with open("compras.txt", "r", encoding="utf-8") as arquivo:
    produtos = arquivo.readlines()
    for i, produto in enumerate(produtos, start=1):
        print(f"{i}. {produto.strip()}")