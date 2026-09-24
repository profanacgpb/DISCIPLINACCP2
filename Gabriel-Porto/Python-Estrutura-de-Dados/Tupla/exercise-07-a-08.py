# 7. Crie uma tupla com números de 0 a 9 (em qualquer ordem) e tente:

numbers_tupla = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)

# a)-
try:
    numbers_tupla [2] = 10
except TypeError:
    print ("Não tem como alterar o valor de uma tupla")
# b)-
print (f"O indíce do número 5: ", numbers_tupla.index(5))

# 8. Crie um dicionário com 5 entradas e suas respectivas chaves e valores.

jogador = {
    "nome": "Neymar", 
    "número": 10, 
    "idade": 34,
    "time_atual": "Santos",
    "valor_mercado": 8.2,
    "atualmente": "Em atividade"
}

print ("\n")
print (f"Chaves: {jogador.keys()}")
print ("\n")

print (f"Valores: {jogador.values()}")
print ("\n")

print (f"Itens: {jogador.items()}")
print ("\n")

print (list(jogador.items())[1])

print (f"dicionário: ",jogador)

for entrada in jogador:
    print (jogador ["nome"], jogador ["número"])
print ("\n")