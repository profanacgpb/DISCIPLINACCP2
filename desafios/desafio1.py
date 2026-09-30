alunos = ["João", "Maria", "Pedro", "Ana", "Carlos"]

print("Lista:", alunos)

alunos.append("Lucas")
print("Adicionando Lucas:", alunos)

alunos.remove("Maria")
print("Removendo Maria:", alunos)

alunos[2] = "Gabriel"
print("Alterando o 3º aluno:", alunos)

print("Primeiros 3:", alunos[:3])

print("Últimos 2:", alunos[-2:])

alunos.reverse()
print("Invertida:", alunos)

alunos.sort()
print("Ordenada:", alunos)