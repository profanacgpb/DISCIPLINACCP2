numero = int(input("Digite um numero:"))

def verificar_par(numero):
    if numero % 2 == 0:
        return True
    else:
        return False
           
if verificar_par(numero):
    print("Numero é par")
else:
    print("Numero é impar")