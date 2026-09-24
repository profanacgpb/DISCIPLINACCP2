# Desafio 2 — Notas 
# Crie uma lista: notas = [7.5, 8.0, 6.5, 9.0, 5.5] 
# Faça: 
# 1. Calcule a maior nota;
# 2. Calcule a menor nota;
# 3. Calcule a quantidade de notas;
# 4. Calcule a soma das notas;
# 5. Calcule a média;
# 6. Ordene as notas;
# 7. Imprima as três maiores notas.

# Crie uma lista: 

notas = [7.5, 8.0, 6.5, 9.0, 5.5] 

# 1. Calcule a maior nota;

maior = max(notas)
print(maior)

# 2. Calcule a menor nota;

menor = min(notas)
print(menor)

# 3. Calcule a quantidade de notas;

quantidade = len(notas)
print(quantidade)

# 4. Calcule a soma das notas;

soma = sum(notas)
print(soma)

# 5. Calcule a média;

media = sum(notas) / len(notas)
print(media)

# 6. Ordene as notas;

notas.sort()
print(notas)

# 7. Imprima as três maiores notas.

print(notas[-3:])

