for loop in range (1, 51, +1): # Estrutura de controle (inicio, fim, passo)
    if loop % 2 == 1: # Condicional para numeros impares
        continue # Comando para pular o resto da repetição atual (vai pular os números impares e deixar apenas os pares)
    print(loop) # Exibição do loop