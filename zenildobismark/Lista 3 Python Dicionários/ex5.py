aluno = {
    'nome' : 'Zenildo',
    'idade' : 26,
    'curso' : 'Ciências da Computação',
    'cidade' : 'Ingá',
    'email' : 'zenildobismarkzbrl@gmail.com',
    'telefone' : 991828820
}

# Crie um programa que verifique se a chave email existe. Se existir, mostre “E-mail cadastrado.”; caso contrário, mostre “E-mail não cadastrado.”

if 'email' in aluno:
    print("Email Cadastrado")
else:
    print('Email não Cadastrado')