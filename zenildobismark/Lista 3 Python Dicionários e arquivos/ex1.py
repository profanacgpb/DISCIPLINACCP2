# Crie um dicionário chamado aluno contendo nome, idade, curso e cidade. 

aluno = {
    'nome' : 'Zenildo',
    'idade' : 26, 
    'curso' : 'Ciências da computação',
    'cidade' : 'Ingá'
}

# a) Imprima o dicionário completo. 
print(aluno)

# b) Imprima apenas o nome.
print(list(aluno.items())[0])
print(list(aluno.keys())[0])
print(aluno['nome'])


# c) Imprima apenas o curso.
print(list(aluno.items())[2])
print(aluno['curso'])