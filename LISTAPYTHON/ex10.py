nome = input("Olá, digite seu nome: ")
idade = int(input(f"{nome}, digite sua idade: "))

if idade >= 12:
    print("Entrada permitida!")
else:
    print("Entrada não permitida")