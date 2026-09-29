#Exercício 5 — Par ou ímpar
def verificar_par(numero):
    if numero % 2 == 0:
        return True
    else:
        return False

numero = int(input("Digite um número: "))

verificar = verificar_par(numero)
print(verificar)