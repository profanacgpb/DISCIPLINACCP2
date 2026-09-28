# Questão 10 - Mini sistema
with open("menu.txt", "w") as menu:
    for i in range(1, 4):
        aluno = input(f"Digite o nome do aluno {i}: ")
        menu.write(f"Aluno {i}: {aluno}\n")

with open("menu.txt", "r") as menu:
    print(menu.read())
