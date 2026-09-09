#vou importar uma biblioteca para o codigo ficar legal
import time

numero = int(input("Digite um numero por favor: "))

for i in range(numero, 0, -1):

#quando tiver aparecendo os numeros no terminal eles vão aparecer a cada 1 segundo ao inves de todos de uma vez.
    print(i)
    time.sleep(1)
print("voce chegou ao fim da sequência")