# Questão 1
nome = input('digite seu nome animal ')
idade = int(input('digite sua idade '))
curso =  input('digite seu curso ')
semestre_atual = int(input('digite seu semestre atual '))
cidade =  input('digite sua cidade ')
estado = input('digite seu estado ')


print (f'olá , {nome} você possui {idade} anos , cursa {curso} e esta no semestre {semestre_atual} voce e da cidade {cidade} que fica no estado {estado}')

# Questão 2

ano = int(input('digite em que ano estamos para calcular sua idade '))
aniversario = int(input('digite em q ano você nasceu '))
idade = ano-aniversario

print (f'você possui {idade} anos de vida ')

# Questão 3 

print ('você esta em uma viagem de carro !')
distancia = float(input('digite a distancia percorrida em km '))
consumo = float(input('digite o consumo medio quantos km seu veiculo faz com um litro '))
litros = distancia / consumo

print (f'você percorreu {distancia} com apenas {litros} litros de combustivel ')

# Questão 4 

valorreal = float(input('digite o valor em real que você deseja converter em dolar e euro '))
dolar = valorreal / 5.25
euro  = valorreal / 6.15

print (f'dolar = {dolar} ')
print (f'euro = {euro} ')

# Questão 5 

frase = input('digite uma palavra ou frase ')
frase0espaço = frase.strip()
fraseM = frase.upper()

print(f'frase modificada {fraseM}')
print(f'quantidade de caracteres {len(frase0espaço)}')

tempython = "python" in frase0espaço.lower()

if tempython:
    print('a palavra tem python ')
else:
    print('a palavra não tem python ')

# Questão 6

palavra = input('digite uma palavra ').strip()
print (f'palavra: {palavra} ')
print (f'quantidade de caracteres {len(palavra)}')
print (f'primeiro caractere{palavra[0]}')
print (f'ultimo caractere {palavra[-1]}')

# Questão 7

nota=float(input('digite sua nota '))
if nota >=9.0 and nota <=10.0 : 
    classificacao='exelente'
elif nota >=7.0:
    classificacao='bom'
elif nota >=5.0:
    classificacao='regular'
elif nota>=0.0 and nota<5.0:
    classificacao='insuficiente'
else:
    classificacao='nota invalida digite um numero entre 0 a 10' 

if nota >= 0.0 and nota<=10.0:
    print(f'Classificação: {classificacao}')
else:
    print(classificacao)

# Questao 8

numero=int(input('digite um numero qualquer'))
if numero % 2 == 0 :
    print('numero par')
else:
    print('impar')

# Questao 9 

n1=int(input('digite um numero '))
n2=int(input('digite outro numero'))

if n1>n2:
    print(f'o numero {n1} é o maior ')
else:
    print(f'o numero {n2} é o maior ')

# Questao 10

valor_prod=float(input('digite o valor do produto em R$ '))

if valor_prod <= 100.00:
    percentual = 0
elif valor_prod <=300.00:
    percentual = 10
else:
    percentual= 15

valordesconto= valor_prod*(percentual/100)
valorfinal= valor_prod - valordesconto

print(f'o valor do desconto foi de {percentual}%')
print(f'o valor do desconto foi {valordesconto}')
print(f' e o valor final da compra ficou {valorfinal}')

