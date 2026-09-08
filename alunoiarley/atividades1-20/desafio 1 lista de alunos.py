alunos=["Alice", "Bob", "Charles", "Pedro", "Lucas"]
print("primeira lista de alunos:", alunos)

alunos.append("maria")
print("após adicionar maria:", alunos)

alunos.remove("Charles")
print("após remover um aluno:", alunos)

alunos[2] = "higor"
print("após substituir o terceiro aluno:", alunos)

print("primeiros três alunos:", alunos[:3])
print("últimos dois alunos:", alunos[-2:])

alunos.reverse()
print("após reverter a lista:", alunos)

alunos.sort()
print("após ordenar a lista:", alunos)