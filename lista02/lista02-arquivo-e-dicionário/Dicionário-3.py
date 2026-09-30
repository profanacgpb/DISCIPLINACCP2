Produtos={ "sapato": 30,
          "Colar": 35,
          "Anel": 70,
          "Camisa": 20.50 ,
          "Short": 15}

#a) Mostrar todos os produtos
for chave in Produtos.keys():
 print(chave)

#b) Mostrar todos os preços
for valor in Produtos.values():
 print(valor)

#c) Mostrar produto e preço
for chave, valor in Produtos.items():
 print(chave, "Valor é: ", valor)

#d) Mostrar o produto mais caro
ValorAlto= max(Produtos, key=Produtos.get)
print(ValorAlto, "é o valor mais Alto sendo um total de: ", Produtos[ValorAlto], "$")