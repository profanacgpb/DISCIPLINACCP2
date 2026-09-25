aluno = {
"nome": "Daniel",
"idade": 18,
"curso": "Ciência da Computação",
"periodo": 2,
"nota": 8.5
}
print(aluno)

#1 - Imprima o nome;
print(aluno["nome"])

#2 - Imprima o curso;
print(aluno["curso"])

#3 - Altere a idade;
aluno["idade"] = 20
print(aluno["idade"])

#4 - Adicione a chave "cidade";
aluno["cidade"] = "São Sebastião de Lagoa de Roça - PB"
print(aluno)

#5 - Percorra todas as chaves;
for chave in aluno.keys():
    print(chave)

#6 - Percorra todos os valores;
for valor in aluno.values():
    print(valor)

#7 - Imprima o Dicionario completo;
print(aluno)