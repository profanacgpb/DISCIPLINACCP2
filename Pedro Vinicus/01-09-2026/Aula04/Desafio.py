#Desafio da Aula 04 sobre criar um programa que receba os segundos e converta em horas,minutos e segundos
segundos= int(input("Quantos segundos:"))


horas = segundos // 3600 #Convertendo em segundos para horas em 3600 pois 1 hora tem 3600 segundos

segundos_resto = segundos % 3600 #Calculando o resto que sobrou ao converter

minutos = segundos_resto // 60 #Convertendo o resto em minutos em 60 pois em 1 minuto tem 60 segundos

segundos_finais = segundos_resto % 60 #Calculando oq sobrou 

print(horas)
print(minutos)
print(segundos_finais)