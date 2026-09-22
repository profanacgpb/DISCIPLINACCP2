nome_arquivo = "meus_numeros.txt"

with open(nome_arquivo, 'w') as f:
    for i in range(1, 11):
        f.write(f"{i}\n")

print("\n9b. Lendo 1 a 10:")
with open(nome_arquivo, 'r') as f:
    print(f.read().strip())

with open(nome_arquivo, 'w') as f:
    for i in range(11, 21):
        f.write(f"{i}\n")

with open(nome_arquivo, 'a') as f:
    for i in range(21, 31):
        f.write(f"{i}\n")

print("\n9e. Lendo 11 a 30 inteiro:")
with open(nome_arquivo, 'r') as f:
    print(f.read().strip())

print("\n9f. Lendo linha por linha:")
with open(nome_arquivo, 'r') as f:
    for linha in f:
        print(linha.strip())