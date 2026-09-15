# Desafio 1 — Lista de alunos 
# Crie uma lista contendo cinco nomes. 
# Faça: 
# 1. Imprima a lista;
# 2. Adicione um sexto aluno;
# 3. Remova um aluno;
# 4. Altere o terceiro nome;
# 5. Imprima os três primeiros nomes;
# 6. Imprima os dois últimos nomes;
# 7. Inverta a lista;
# 8. Ordene a lista em ordem alfabética.

alunos = ['Zenildo', 'Bismark', 'Rodrigues', 'da', 'Luz']

# 1. Imprima a lista;

print(alunos)

# 2. Adicione um sexto aluno;

alunos.append('Alice')
print(alunos)

# 3. Remova um aluno;

alunos.remove('da')
print(alunos)

# 4. Altere o terceiro nome;

alunos[3] = 'Fernandes'
print(alunos)

# 5. Imprima os três primeiros nomes;

print(alunos[:3])

# 6. Imprima os dois últimos nomes;

print(alunos[-2:])

# 7. Inverta a lista;

alunos.reverse()
print(alunos)

# 8. Ordene a lista em ordem alfabética.

alunos.sort()
print(alunos)