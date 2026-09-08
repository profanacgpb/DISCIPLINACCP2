nome=input("Digite seu nome: ")
idade=int(input('Digite sua idade: '))
nota=float(input("Digite sua nota: "))

print(f"{nome}")
print(f"{idade}")
print(f"{nota}")

if idade >=18 :
    print("Maior de idade.")
else:
    print("Menor de idade.")

if nota >= 7 :
    print("Aprovado")
else:
    print("Reprovado")

