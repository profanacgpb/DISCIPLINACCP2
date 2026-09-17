# Cadastro com dicionário
print ("\n")
aluno_nassau = {
    "nome": "Gabriel",
    "idade": 19,
    "curso": "Ciência da Computação",
    "periodo": 2,
    "nota": 8.2,
    "cidade": "Campina Grande-PB"
}

print (aluno_nassau["nome"])
print (aluno_nassau["curso"])

print ("\n")
for chaves in aluno_nassau:
    print (chaves)
print ("\n")
for valores in aluno_nassau.values():
    print (valores)
print ("\n")