produtos= {
    "notebook": "2500",
    "mouse": "100",
    "carregador": "100",
    "fone": "120",
    "teclado": "400"
}
print(produtos)
for produto in produtos.keys():
    print(produto)
for valores in produtos.values():
    print (valores)

valorAlto= max(produtos, key=produtos.get)
print(valorAlto, "é o valor mais alto sendo um total de:", produtos[valorAlto])

