aluno = {
    'nome' : 'Zenildo',
    'idade' : 26,
    'curso' : 'Ciências da Computação',
    'cidade' : 'Ingá'
}

# Adicione ao dicionário as informações email e telefone. Depois imprima todas as informações.
aluno['email'] = 'zenildobismarkzbrl@gmail.com'
aluno['telefone'] = 83991828820

print(aluno)

# Remova a informação telefone do dicionário e imprima o resultado.
del aluno['email']
aluno.pop('telefone')
aluno.pop('nome')

print(aluno)