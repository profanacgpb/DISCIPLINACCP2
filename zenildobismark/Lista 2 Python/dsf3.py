# Desafio 3 — Cadastro com dicionário 
# Crie um dicionário representando um aluno: 
# aluno = { "nome": "Maria", "idade": 22, "curso": "ADS", "periodo": 4, "nota": 8.5 } 
# Faça: 
# 1. Imprima o nome;
# 2. Imprima o curso;
# 3. Altere a idade;
# 4. Adicione a chave "cidade";
# 5. Percorra todas as chaves;
# 6. Percorra todos os valores;
# 7. Percorra chave e valor;
# 8. Imprima o dicionário completo.

# Crie um dicionário representando um aluno: 
aluno = {
            "nome": "Maria", 
            "idade": 22, 
            "curso": "ADS", 
            "periodo": 4, 
            "nota": 8.5 
        } 

# 1. Imprima o nome;

print(aluno['nome'])

# 2. Imprima o curso;

print(aluno["curso"])

# 3. Altere a idade;

aluno['idade'] = 26
print(aluno['idade'])

# 4. Adicione a chave "cidade";

aluno['cidade'] = 'inga'
print(aluno['cidade'])

# 5. Percorra todas as chaves;

for chave in aluno:
    print(chave)

# 6. Percorra todos os valores;

for valor in aluno.values():
    print(valor)

# 7. Percorra chave e valor;

for chave, valor in aluno.items():
    print(f'{chave} : {valor}')

# 8. Imprima o dicionário completo.

print(aluno)