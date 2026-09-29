# Crie um dicionário com 5 produtos e seus preços. 
produtos = {
    'cafe' : 20,
    'leite' : 12,
    'cuscuz' : 5,
    'arroz' : 7,
    'feijao' : 25
}
# Faça: 
# a) mostrar todos os produtos;
print(produtos)

# b) mostrar todos os preços;
print(f'PREÇOS: {list(produtos.values())}') 

# c) mostrar produto e preço; 
for chave, valor in produtos.items():
    print(f'Produtos: {chave} || Preço: {valor}')

# d) mostrar o produto mais caro.
maior = 0

for chave, valor in produtos.items():
    if valor > maior:
        maior = valor
        produto = chave


print(f'Produto mais caro: {produto} - R$ {maior:.2f}')