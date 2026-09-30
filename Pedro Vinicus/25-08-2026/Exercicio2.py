esc = int(input('Digite qual opção deseja usar (1 ou 2): '))
if esc ==1:
    numero = int(input('Digite o multiplicando: '))
    for mult in range(1,11):
        print(f'{numero} x {mult} = {numero * mult}')
elif esc == 2:
    numero = int(input('Digite o numero: '))
i=0
while i<=10:
    res = numero * i
    print(f'{numero} x {i} = {res}')
    i+=1