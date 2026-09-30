def verificar_par():
    return numero % 2== 0
numero= int(input("Digite seu numero: "))
if verificar_par():
    print("Seu numero é par")
else:
    print("Seu numero é impar")