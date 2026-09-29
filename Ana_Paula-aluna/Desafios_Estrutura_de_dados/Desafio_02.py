#Desafio 2: Análise de notas

notas = [7.5, 8.0, 6.5, 9.0, 5.5]
print("NOTAS REGISTRADAS:", notas)

media = sum(notas)/len(notas) 
print("\n")

notas.sort()
print("Lista de notas ordenada:", notas)
print("MENOR NOTA:", notas[0])
print("MAIOR NOTA:", notas[-1])

print("Quantidade de notas na lista:", len(notas))
print("Soma das notas:", sum(notas))
print(f"Média das notas: {media}")
print("As 3 maiores notas são:", notas[:3])
