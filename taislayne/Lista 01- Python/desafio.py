nome = input("Digite seu nome: ")
idade= int(input("Digite sua idade: "))
nota= float(input("Digite sua nota: "))

print(f"Olá, o seu nome é {nome}, sua idade é {idade} e sua nota é {nota}")

if idade >= 18:
    print(f"{nome} é maior de idade.")
else:
    print(f"{nome} é menor de idade.")

if nota >= 7:
    print(f"{nome} foi aprovado.")
else:
    print(f"{nome} foi reprovado.")