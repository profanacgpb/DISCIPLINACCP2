# Números:

arquivo = open ("Gabriel-Porto/Python-Estrutura-de-Dados/Arquivos/Questão-01-a-10/numeros.txt", "w")

for numbers in range (1, 21, +1):
    arquivo.write(str(numbers) + "\n") # Conversão o arquivo é txt

arquivo.close()

arquivo = open ("Gabriel-Porto/Python-Estrutura-de-Dados/Arquivos/Questão-01-a-10/numeros.txt", "r")

exibicao_numbers = arquivo.read()
print (exibicao_numbers)

arquivo.close()
