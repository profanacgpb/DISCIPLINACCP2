# contagem regressiva começando do 5
import time
n = (input('Digite qualquer coisa para uma contagem regressiva começando do 5: '))

for i in range(5,-0,-1):
    if i < 1:
        break
    time.sleep(1)
    print(i)