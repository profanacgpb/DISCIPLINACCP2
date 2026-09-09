#Desafio 2: Análise de notas

notas = [7.5, 8.0, 6.5, 9.0, 5.5]
print("NOTAS REGISTRADAS:", notas)
print("\n")

media = sum(notas)/len(notas) 

notas.sort()

print("MENOR NOTA:", notas[0])
print("MAIOR NOTA:", notas[4])
print("Quantidade de notas na lista:", len(notas))
print("Soma das notas:", sum(notas))
print(f"Média das notas: {media}")
print("Lista de notas ordenada:", notas)

notas.reverse()
print("As 3 maiores notas são:", notas[:3])




