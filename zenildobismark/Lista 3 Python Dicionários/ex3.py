aluno = {
    'nome' : 'Zenildo',
    'idade' : 26,
    'curso' : 'Ciências da Computação',
    'cidade' : 'Ingá'
}

# Adicione ao dicionário as informações email e telefone. Depois imprima todas as informações.
aluno['email'] = 'zenildobismarkzbrl@gmail.com'
aluno['telefone'] = 83991828820

for chave, valor in aluno.items():
    print(f'Chave: {chave} || Valor: {valor}')