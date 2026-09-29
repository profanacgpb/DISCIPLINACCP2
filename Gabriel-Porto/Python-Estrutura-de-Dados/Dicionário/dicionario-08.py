# Crie um dicionário com 5 produtos e seus preços:

produtos_mercado = {
    "Arroz (5kg)": 24.90,
    "Feijão Carioca (1kg)": 7.50,
    "Café Torrado (500g)": 18.20,
    "Leite Integral (1L)": 5.49,
    "Óleo de Soja (900ml)": 6.80
}

# a) mostrar todos os produtos:

print ("Todos os produtos do estoque logo abaixo:")

for nome_produto, preco in produtos_mercado.items():
    print (f"{nome_produto}")
print ("\n")

# b) mostrar todos os preços:

print ("Todos os preços do estoque (respectivamente):")

for preco_produto in produtos_mercado.values():
    print (f"{preco_produto:.2f}")
print ("\n")

# c) mostrar produto e preço:

print ("Todos os produtos e preços do estoque:")

for nome_produto, preco_produto in produtos_mercado.items():
    print (f"{nome_produto} R$ {preco_produto:.2f}")
print ("\n")

# d) mostrar o produto mais caro:

maior_valor = max(produtos_mercado, key=produtos_mercado.get)

print (maior_valor, produtos_mercado[maior_valor])