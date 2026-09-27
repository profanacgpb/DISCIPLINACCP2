def somar(a,b):
    return a+b
def subtrair(a,b):
    return a-b
def multiplicar(a,b):
    return a*b
def dividir(a,b):
    if b ==0:
        return "não é possivel dividir por zero"
    return a/b

while True:
    print("\n===== CALCULADORA =====")
    print("1 - Somar")
    print("2 - Subtrair")
    print("3 - Multiplicar")
    print("4 - Dividir")
    print("5 - Sair")

    opção = int(input("escolha uma opção:"))

    if opção==5:
        print("programa encerrado")
        break

    numero1= int(input("digite o primeiro numero: "))
    numero2= int(input("digite o segundo numero: "))

    if opção==1:
        resultado= somar(numero1,numero2)
        print("resultado:", resultado)
    elif opção==2:
        resultado= subtrair(numero1,numero2)
        print("resultado:", resultado)
    elif opção==3:
        resultado= multiplicar(numero1,numero2)
        print("resultado:", resultado)
    elif opção==4:
        resultado= dividir(numero1,numero2)
        print("resultado:", resultado)
    else:
        print("opção invalida")
    
    

