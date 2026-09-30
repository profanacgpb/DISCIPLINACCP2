# Append:

arquivo = open ("Gabriel-Porto/Python-Estrutura-de-Dados/Arquivos/Questão-01-a-10/numeros.txt", "a")

for numbers in range (21, 31, +1):
    arquivo.write(str(numbers) + "\n")

arquivo.close()

arquivo = open ("Gabriel-Porto/Python-Estrutura-de-Dados/Arquivos/Questão-01-a-10/numeros.txt", "r")

exibicao_numbers = arquivo.read()
print (exibicao_numbers)

arquivo.close ()