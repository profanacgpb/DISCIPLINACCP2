# 6. Crie o dicionário abaixo e utilize for e items() para apresentar cada chave e valor:

produto = {
    "nome": "Notebook", 
    "preco": 2500, 
    "marca": "Acer"
}

for chaves in produto.keys():
    print (chaves)

for valores in produto.values():
    print (valores)