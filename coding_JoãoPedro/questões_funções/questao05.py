nota1 = float(input("Nota 1: "))
nota2 = float(input("Nota 2: "))
nota3 = float(input("Nota 3: "))

media = (nota1 + nota2 + nota3) /3

print(f"Média: {media}")

if media >=7:
    print("Situação: Aprovado")
elif media >=5:
    print("Situação: Recuperação")
else:
    print("Situação: Reprovado")