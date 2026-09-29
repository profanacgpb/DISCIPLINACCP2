notas = [7.5, 8.0, 6.5, 9.0, 5.5]

print("1. Maior nota:", max(notas))

print("2. Menor nota:", min(notas))

print("3. Quantidade de notas:", len(notas))

print("4. Soma das notas:", sum(notas))

media = sum(notas) / len(notas)
print("5. Média:", media)

NotasOrdenadas = sorted(notas)         
print("6. Notas ordenadas:", NotasOrdenadas)

TresMaiores = sorted(notas, reverse=True)[:3]
print("7. Três maiores notas:", TresMaiores)