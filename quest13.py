# programa começa pedindo um número ao usuário.

numero = int(input("Digite um número: "))

# a partir do numero digitado o proogrma cria um laço de repetição que vai ate o 10 

for i in range(1, 11):

# vai multiplicar o numero digitado pelo mesmo numero que esta na sequencia do laço de repetição

    tabuada = numero * i

# mostra a tabuada no terminal com o comando print.


    print(numero, "x", i, "=", tabuada)
    