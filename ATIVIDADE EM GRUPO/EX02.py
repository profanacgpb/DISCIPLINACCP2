notas = [7.5, 8.0, 6.5, 9.0, 5.5]

print("Maior nota:", max(notas))
print("Menor nota:", min(notas))

print("Quantidade:", len(notas))

print("Soma:", sum(notas))

media = sum(notas) / len(notas)
print("Média:", media)

notas.sort()
print("Notas ordenadas:", notas)

print("3 maiores:", notas[-3:])