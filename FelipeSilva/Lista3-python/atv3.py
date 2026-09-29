aluno={
    "nome": "Felipe",
    "idade": 18,
    "curso": "CC",
    "periodo": 2,
    "nota": 10
}

print(f"Nome: {aluno['nome']}")
print(f"Curso: {aluno['curso']}")
aluno["idade"] = 23
aluno["cidade"] = "Ingá"
print("Chaves: ")
for chave in aluno.keys():
    print("chave")
print("Valores: ")
for valor in aluno.values():
    print(valor)
print("Chave e valor: ")
for chave, valor in aluno.items():
    print(f"{chave}: {valor}")

print("Dicionário completo: ")
print(aluno)