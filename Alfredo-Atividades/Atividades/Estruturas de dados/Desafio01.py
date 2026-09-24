alunos = ["Alfredo", "Pain", "Fusca", "Jozão", "Kyll"]

print("Lista original:")
print(alunos)

alunos.append("Lucas")
print("\nApós adicionar Lucas:")
print(alunos)

alunos.remove("Pain")
print("\nApós remover Pain:")
print(alunos)

alunos[2] = "Emmanuel"
print("\nApós alterar o terceiro nome:")
print(alunos)

print("\nTrês primeiros nomes:")
print(alunos[:3])

print("\nDois últimos nomes:")
print(alunos[-2:])

alunos.reverse()
print("\nLista invertida:")
print(alunos)

alunos.sort()
print("\nLista em ordem alfabética:")
print(alunos)