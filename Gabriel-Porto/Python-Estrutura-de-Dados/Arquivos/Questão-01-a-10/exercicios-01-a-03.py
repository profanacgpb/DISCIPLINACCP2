# Obs: # O 'with' abre o arquivo e o fecha automaticamente no final do bloco
# with open("alunos.txt", "w", encoding="utf-8") as arquivo: 
from time import sleep

# Obs: dependendo o metodos se você for escrever ler ou coisa do tipo tem que fechar o arquivo

# Escrevendo em um arquivo (Primeiro arquivo):

arquivo = open ("Gabriel-Porto/Python-Estrutura-de-Dados/Arquivos/Questão-01-a-10/alunos.txt", "w")

for nome in range (1, 6, +1):
    nome_entrada = input(f"Digite um nome qualquer ({nome}): ")
    arquivo.write(nome_entrada + "\n")
arquivo.close()

# Lendo um arquivo (Leitura):

arquivo = open ("Gabriel-Porto/Python-Estrutura-de-Dados/Arquivos/Questão-01-a-10/alunos.txt", "r")
exibicao_conteudo = arquivo.read()
print (exibicao_conteudo)
arquivo.close()

# Lendo um arquivo linha por linha (Linha por linha):

arquivo = open ("Gabriel-Porto/Python-Estrutura-de-Dados/Arquivos/Questão-01-a-10/alunos.txt", "r")

print ("Lista Alunos: ")

for linha in arquivo:
    sleep(0.5)
    print (linha.strip())
arquivo.close()