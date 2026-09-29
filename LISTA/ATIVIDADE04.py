#1- Crie um arquivo chamado alunos.txt e escreva nele os nomes de 5 alunos.
with open("alunos.txt", "w") as arquivo:
    arquivo.write("Kaynan\nCSara\nGabriel\nDaniel\nPedro\n")
print("Arquivo 'alunos.txt' criado com 5 nomes.")
#2- Leia o arquivo alunos.txt e imprima todos os nomes na tela.
with open("alunos.txt", "r") as arquivo:
    conteudo = arquivo.read()
    print("Conteúdo de alunos.txt:")
    print(conteudo.strip())
#3- Leia o arquivo alunos.txt e apresente os nomes um por vez, por exemplo: Aluno: Ana.
with open("alunos.txt", "r") as arquivo:
    for linha in arquivo:
        print(f"Aluno: {linha.strip()}")
#4- Crie numeros.txt, escreva os números de 1 a 20, um por linha, e depois leia e mostre os números.
with open("numeros.txt", "w") as arquivo:
    for i in range(1, 21):
        arquivo.write(str(i) + "\n")
with open("numeros.txt", "r") as arquivo:
    print("Números de 1 a 20 cadastrados com sucesso.")
#5- Utilizando o arquivo da questão anterior: 
# a) adicione os números de 21 a 30; 
# b) leia o arquivo; 
# c) mostre todos os números.
with open("numeros.txt", "a") as arquivo:
    for i in range(21, 31):
        arquivo.write(str(i) + "\n")
print("Mostrando todos os números do arquivo (1 a 30):")
with open("numeros.txt", "r") as arquivo:
    todos_numeros = [linha.strip() for linha in arquivo]
    print(", ".join(todos_numeros))
#6- Crie mensagem.txt, escreva “Primeira mensagem” e depois, usando o modo w, substitua por “Nova mensagem”. 
# Leia o arquivo e verifique o resultado.
with open("mensagem.txt", "w") as arquivo:
    arquivo.write("Primeira mensagem\n")
with open("mensagem.txt", "w") as arquivo:
    arquivo.write("Nova mensagem\n")
with open("mensagem.txt", "r") as arquivo:
    print("Conteúdo final de mensagem.txt:", arquivo.read().strip())
#7- Crie um programa que permita ao usuário cadastrar nomes. Os nomes devem ser armazenados no arquivo alunos.txt.
novo_aluno = input("Digite o seu nome: ")
with open("alunos.txt", "a") as arquivo:
    arquivo.write(novo_aluno + "\n")
print(f"O aluno(a) {novo_aluno} foi adicionado ao arquivo alunos.txt.")
#8- Crie um programa que permita cadastrar 5 produtos em compras.txt. 
# Depois leia o arquivo e apresente os produtos numerados.
lista_compras = ["Arroz", "Feijão", "Macarrão", "Carne", "Leite"]
with open("compras.txt", "w") as arquivo:
    for item in lista_compras:
        arquivo.write(item + "\n")

print("Lista de Compras Numerada:")
with open("compras.txt", "r") as arquivo:
    for indice, linha in enumerate(arquivo, start=1):
        print(f"{indice} - {linha.strip()}")
#9- Crie notas.txt e armazene dados no formato Ana;8.5. 
# Depois leia o arquivo e mostre cada aluno e sua nota.
with open("notas.txt", "w") as arquivo:
    arquivo.write("Gabriel;8.5\nDaniel;7.0\nKaynan;9.5\n")

with open("notas.txt", "r") as arquivo:
    for linha in arquivo:
        nome, nota = linha.strip().split(";")
        print(f"Aluno: {nome} | Nota: {nota}")