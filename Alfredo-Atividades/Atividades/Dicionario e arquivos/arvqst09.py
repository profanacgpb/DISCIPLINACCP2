with open("notas.txt", "w", encoding="utf-8") as arquivo:
    dados = [
        "Alfredo;8.5",
        "Oswaldo;7.0",
        "Jegue;9.2",
        "Pain;6.5"
    ]
    for linha in dados:
        arquivo.write(linha + "\n")

print("Arquivo notas.txt criado com sucesso!\n")

print("Notas dos alunos:")
with open("notas.txt", "r", encoding="utf-8") as arquivo:
    for linha in arquivo:
        nome, nota = linha.strip().split(";")
        print(f"Aluno: {nome} - Nota: {nota}")