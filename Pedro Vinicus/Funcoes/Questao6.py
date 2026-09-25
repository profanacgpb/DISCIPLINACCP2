numero1=int(input("Digite seu primeiro numero:"))
numero2=int(input("Digite seu segundo numero:"))
numero3=int(input("Digite seu terceiro numero:"))

numeros = numero1, numero2,numero3

def maior(numeros):
    maior_numero = numeros[0]
    for numero in numeros:
       if numero > maior_numero:
           maior_numero = numero
    return maior_numero
           
   

print(f"O maior numero é:{maior(numeros)}")