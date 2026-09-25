print("========Exercicio 1 ======")
nomes = ["Porto", "Daniel", "Ana", "Pedru AEEEEEW", "Alfredinhu"]

print(nomes)

nomes.append("Stella")
print(nomes)

nomes.remove("Alfredinhu")
print(nomes)

nomes[2] = "gabriel jamily"

print(nomes)

print("3 primeiros:", nomes[:3])
print("2 ultimos:", nomes[-2:])

print("Ordenando:", sorted(nomes))
nomes.reverse()
print("Invertida:", nomes)
print("========Exercicio 2======")

notas = [7.5,8.0,6.5,9.0,5.5]

print("Maior nota:", max(notas))
print("Menor nota:", min(notas))
print("Quantidade", len(notas))
print("Soma:", sum(notas))
print("Média:", sum(notas) / len(notas))

ordenadas = sorted(notas)
print("Notas Ordenadas:", ordenadas)
print("3 maiores:", ordenadas[-3:])