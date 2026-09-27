def maior_numero(a,b,c):
    if a>=b and a>=c:
        return a
    elif b>=c and b>=a:
        return b
    else:
        return c

numero1 =int(input("primeiro numero:"))
numero2 =int(input("segundo numero:"))
numero3 =int(input("terceiro numero:"))

maior = maior_numero(numero1,numero2,numero3)
print("maior numero:", maior)


   
