nome_alu = input("Qual o seu nome? ")
idade = int(input("Qual a sua idade? "))
nota = float(input("Qual a sua nota? "))

print(f"Nome: {nome_alu}")
print(f"Idade: {idade}")

if idade >= 18:
    print("Situação: Maior de idade")
else:
    print("Situação: Menor de idade")

if nota >= 7:
    print("Resultado: Aprovado")
else:
    print("Resultado: Reprovado")