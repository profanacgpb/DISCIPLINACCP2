notas = [7.5, 8.0, 6.5, 9.0, 5.5]
maior = max(notas)
menor = min(notas)
print(maior, menor)

quanti = len(notas)
print(quanti)

somar = notas[0] + notas[1] + notas[2] + notas[3] + notas[4]
print(somar)

media = somar / 5
print(media)

notas.sort()
print(notas)