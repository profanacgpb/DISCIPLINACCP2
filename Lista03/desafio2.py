notas = [7.5, 8.0, 6.5, 9.0, 5.5]

#1 - Calcule a maior nota;
maior_nota = max(notas)
print(maior_nota)

#2 - Calcule a menor nota;
menor_nota = min(notas)
print(menor_nota)

#3 - Calcule a quantidade de notas;
quant_nota = len(notas)
print(quant_nota)

#4 - Calcule a soma das notas;
soma_nota = sum(notas)
print(soma_nota)

#5 - Calcule a media;
media_nota = soma_nota / quant_nota
print(media_nota)

#6 - Ordene as notas
notas.sort()
print(notas)

#7 - Imprima as três maiores notas
print(notas[:3])