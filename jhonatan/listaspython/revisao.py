# Questao 11 
for a in range (1,21):
    print(a)

# Questao 12

for a in range (2,51,2):
    print (a)

#Questao 13 

soma=0
for a in range (1,101):
    soma +=a

print(f' a soma é {soma}')

#Questao 14

numero=int(input('digite um numero de 0 a 10 '))
limite=int(input('digite o limete da calculadora '))

print(f'\n tabuada do numero {numero} (ate {limite} )')

for a in range (1, limite ,+ 1):
    resultado=numero * a
    print(f'{numero} X {a} = {resultado}')

#Questao 15 

contador = 0
while contador <= 10:
    print(contador)
    contador+=1

#Questao 16
senhacorreta="jojolindo09"
senha=input('digite a senha ')

while senha != senhacorreta:
    print('senha incorreta !! tente novamente : ')
    senha = input ('digite a senha novamente ')
print('acesso permitido ')