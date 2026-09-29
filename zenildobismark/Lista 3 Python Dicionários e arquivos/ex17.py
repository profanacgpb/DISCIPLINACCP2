# Crie notas.txt e armazene dados no formato Ana;8.5. 
# Depois leia o arquivo e mostre cada aluno e sua nota.

with open('notas.txt', 'w', encoding='utf-8') as arquivo:
    arquivo.write("Ana;8.5\n")
    arquivo.write("Carlos;7.0\n")
    arquivo.write("Beatriz;9.2\n")

with open('notas.txt', 'r', encoding='utf-8') as arquivo:
    for linha in arquivo:
        nome, nota = linha.strip().split(';')
        print(f"Aluno(a): {nome} - Nota: {nota}")