produtos = {
    "Arroz": 7.00,
    "Feijão": 8.00,
    "Macarrão": 5.00,
    "Leite": 6.50,
    "Café": 15.00
}

for produto in produtos:
    print(produto)

for preço in produtos.values():
    print(preço)

for produto, preço in produtos.items():
    print(produto, "->", preço)

print ("Produto mais caro:")
produto_caro = max(produtos, key=produtos.get)

print (produto_caro, "->", produtos[produto_caro])