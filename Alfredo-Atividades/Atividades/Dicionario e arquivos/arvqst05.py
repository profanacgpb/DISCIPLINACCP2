with open("numeros.txt", "a", encoding="utf-8") as arquivo:
    for i in range(21, 31):
        arquivo.write(f"{i}\n")

print("Números de 21 a 30 adicionados!")

print("\nTodos os números no arquivo:")
with open("numeros.txt", "r", encoding="utf-8") as arquivo:
    for linha in arquivo:
        print(linha.strip())