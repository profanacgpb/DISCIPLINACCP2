with open("numeros.txt", "w", encoding="utf-8") as arquivo:
    for i in range(1, 21):
        arquivo.write(f"{i}\n")

print("Arquivo numeros.txt criado!")

print("\nNúmeros no arquivo:")
with open("numeros.txt", "r", encoding="utf-8") as arquivo:
    for linha in arquivo:
        print(linha.strip())