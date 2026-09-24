#Exercicio4 da aula04 sobre Use // e % para converter minutos em horas e minutos

minutos = int(input("Quantos minutos:")) #Variavel recebe o valor
horas = minutos // 60 #Converte os minuto em horas 
minutos_resto = minutos % 60 #pega o resto que sobrou ao converter

print("Horas:",horas)
print("Minutos:",minutos_resto)
