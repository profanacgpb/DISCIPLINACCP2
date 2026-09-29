alunos = ["Zena", "Ana", "Daniel", "Eduardo", "Jonta"]

print(f"Lista inicial: {alunos}")

alunos.append("Felipe")

print(f"Agora {alunos} foi modificado.")

alunos.remove("Ana")

print(f"Após remover: {alunos}")

alunos[2] = "Gabriel"

print(f"Após alterar o 3º aluno: {alunos}")

print(f"Primeiros 3: {alunos[:3]}")

print(f"Últimos 2: {alunos[-2:]}")

alunos.reverse()

print(f"Lista invertida: {alunos}")

alunos.sort()

print(f"Lista ordenada: {alunos}")