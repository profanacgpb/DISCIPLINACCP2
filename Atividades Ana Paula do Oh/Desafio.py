Nomes = {
    "Ana": "Ana",
}
Idade = {
    "Idade": 20
}
Curso = {
    "Curso": "Engenharia"
}
dados = [Nomes, Idade, Curso]
arquivo  = open("dados.txt", "w")
for dado in dados:
    arquivo.write(str(dado) + "\n")
arquivo.write("\n")
