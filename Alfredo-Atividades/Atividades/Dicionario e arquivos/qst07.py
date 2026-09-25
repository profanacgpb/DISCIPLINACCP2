aluno = {
    "nome": "João",
    "nota1": 8,
    "nota2": 6
}

media = (aluno["nota1"] + aluno["nota2"]) / 2

print(f"Aluno: {aluno['nome']}")
print(f"Média: {media}")

if media >= 7:
    print("Aprovado")
else:
    print("Reprovado")