def verificar_par(numero):
    return numero%2==0

numero= int(input("digite seu numero"))
resultado= verificar_par(numero)

if resultado:
    print("o numero é par")
else:
    print("o numero é impar")