# Passo 1: Criar dois dicionarios com os dados
aluno1 = {
    "nome": "Ana",
    "idade": "20",
    "curso": "CC"
}

aluno2 = {
    "nome": "Mussum",
    "idade": "43",
    "curso": "Artes visuais"
}


lista_alunos = [aluno1, aluno2]


arquivo = open("sistema_cadastro.txt", "a")

for item in lista_alunos:
    linha = item["nome"] + ", " + item["idade"] + ", " + item["curso"] + "\n"
    arquivo.write(linha)

arquivo.close()

print("Cadastros salvos com sucesso!")