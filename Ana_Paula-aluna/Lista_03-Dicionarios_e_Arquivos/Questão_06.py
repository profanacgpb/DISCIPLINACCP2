#QUESTÃO 6 - Questão 6 — Percorrendo o dicionário
#Crie o dicionário abaixo e utilize for e items() para apresentar cada chave e valor:
#produto = {" + '"nome": "Notebook", "preco": 2500, "marca": "Acer", "estoque": 10' + "}

produto = {"nome": "Notebook", "preco": 2500, "marca": "Acer", "estoque": 10}
print(produto)

for chave, valor in produto.items():
    print(chave,"->",valor)