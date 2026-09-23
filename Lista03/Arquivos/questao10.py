from itertools import count
import time

print("Selecione uma das opções abaixo:")
print("        1 - Cadastrar aluno")
print("        2 - Listar alunos")
print("        3 - Sair")
entrada = int(input("Digite aqui: "))

if entrada == 1:
    with open("minisistema.txt", "a") as arquivo:
        for cad in count(start=1, step=1):
            cadastro = input("Digite aqui o nome do aluno a ser cadastrado: ").lower()
            arquivo.write(f"{cad+1} - {cadastro}\n")
            if cadastro == "sair":
                break
elif entrada == 2:
    with open("minisistema.txt", "r") as arquivo:
        nomes = arquivo.read()
        print(nomes)
else:
    print("Sistema encerrado!")