
#Exercicio1 da aula 4 calcule o preço final com desconto#

preco_original = float(input("Digite o preço original do produto: ")) #Pegando o preço do produyto
percentual_desconto = float(input("Digite o percentual de desconto (em %): ")) #Pegando o desconto oferecido

preco_descontado = preco_original - (preco_original * percentual_desconto / 100)
#Realizando o calculo aonde a variavel ele vai receber um calculo aonde faz a multiplicação
# dos dois valores e dividir por 100
print("O preço com desconto é: R$", f"{preco_descontado:.2f}")
