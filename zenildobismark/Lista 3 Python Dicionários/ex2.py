# Utilize o dicionário da questão anterior.
aluno = {
    'nome' : 'Zenildo',
    'idade' : 26,
    'curso' : 'Ciências da Computação',
    'cidade' : 'Ingá'
}

# a) Altere a idade do aluno.
aluno['idade'] = 30
print(list(aluno.items())[1])

# b) Altere o curso.
aluno['curso'] = 'Administração'
print(list(aluno.items())[2])

# c) Imprima o dicionário novamente.
for chave, valor in aluno.items():
    print(f"Chave: {chave} || Valor: {valor}")
