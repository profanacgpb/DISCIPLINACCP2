# Crie o dicionário abaixo e utilize for e items() para apresentar cada chave e valor:
#   
produto = {
    "nome": "Notebook", 
    "preco": 2500, 
    "marca": "Acer", 
    "estoque": 10
}

for chave, valor in produto.items():
    print(f'Chave: {chave} || Valor: {valor}')