nomes = ["Daniel", "Gabriel", "Kaynan", "Pedro", "Paulo"]

#1 - Imprima a lista
print(nomes)

#2 - Adicone um sexto aluno
nomes.append("Kauan")
print(nomes)

#3 - Remova um aluno
nomes.remove(nomes[1])
print(nomes)

#4 - Altere o terceiro nome
nomes[3] = "Alfredo"
print(nomes)

#5 - Imprima os 3 primeiros nomes
print(f"Os 3 primeiros nomes da lista são: {nomes[0], nomes[1], nomes[2]}")

#6 - Imprima os 2 ultimos nomes
print(f"Os 2 ultimos nomes da lista são: {nomes[3], nomes[4]}")

#7 - Inverta a lista
nomes.reverse()
print(nomes)

#8 - Ordene a lista em ordem alfabética
nomes.sort()
print(nomes)