#Desafio 1: Lista de alunos

nomes = ["Carlos", "Eduarda", "Ana", "Daniel", "Bia"]
print("NOMES:", nomes)

nomes.append("Fábio")
print("\nNovo nome na lista:", nomes)

nomes.remove("Daniel")
print("Retirada de um nome:", nomes)

nomes.insert(2,"Carla")
print("Alteração do 3º nome:", nomes)

print("Os 3 primeiros nomes da lista são:", nomes[:3])

i = len(nomes)
print("Os dois últimos nomes da lista são:", nomes[i-2:i])

nomes.sort()
print ("Lista ordenada:", nomes)

nomes.reverse()
print("Lista invertida:", nomes)
