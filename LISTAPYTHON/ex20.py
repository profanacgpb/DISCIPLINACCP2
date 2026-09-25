nome = input("Olá aluno, digite seu nome: ")
idade = int(input(f"{nome}, digite sua idade: "))
nota = int(input(f"{nome}, digite sua nota: "))

print(f"Nome: {nome}")
print(f"Idade: {idade}")

if idade >= 18:
    print(f"{nome}, você é maior de idade, pois possui {idade} anos de idade!")
else:
    print(f"{nome}, você é menor de idade, pois possui {idade} anos de idade!")

if nota >= 7:
    print(f"Parabéns, {nome} você foi APROVADO!")
else:
    print(f"Que pena {nome}, você foi REPROVADO!")

