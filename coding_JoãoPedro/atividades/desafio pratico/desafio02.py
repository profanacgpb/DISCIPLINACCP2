notas = [7.5, 8.0, 6.5, 9.0, 5.5]

maior = max(notas)
print(maior)

menor = min(notas)
print(menor)

quantidade = len(notas)
print(quantidade)

soma = sum(notas)
print(soma)

media = soma/quantidade
print(media)

notas.sort()
print(notas)

maiores = notas [-3:]
print(maiores)