aluno = {
    "nome": "Maria",
    "idade": 22,
    "curso": "ADS",
    "periodo": 4,
    "nota": 8.5
}

print(aluno["nome"])

print(aluno["curso"])

aluno["idade"] = 23

aluno["cidade"] = "São Paulo"

print("\nChaves:")
for chave in aluno:
    print(chave)

print("\nValores:")
for valor in aluno.values():
    print(valor)

print("\nChave e valor:")
for chave, valor in aluno.items():
    print(chave, "=", valor)

print("\nDicionário completo:")
print(aluno)