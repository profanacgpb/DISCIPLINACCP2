nome = input("Digite o nome do aluno: ")
idade = int(input("Digite a idade do aluno: "))
nota = float(input("Digite a nota do aluno: "))

print("\n--- DADOS DO ALUNO ---")
print("Nome:", nome)
print("Idade:", idade)
print("Nota:", nota)

if idade >= 18:
    print("O aluno é maior de idade.")
else:
    print("O aluno é menor de idade.")

if nota >= 7:
    print("O aluno foi aprovado.")
else:
    print("O aluno foi reprovado.")