# Crie verificar_par(numero). 
# Retorne True se o número for par e False caso contrário. 
# Use o resultado para apresentar uma mensagem ao usuário.

def verificar_par(numero):
    if numero % 2 == 0:
        return "O número é PAR!"
    else:
        return "O número é ÍMPAR!"

print(verificar_par(8))
print(verificar_par(3))