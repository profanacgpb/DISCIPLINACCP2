#Faça um programa que receba uma quantidade de segundos e converta para horas, minutos e segundos.
sec = int(input("Digite os segundos: "))
h = sec // 3600
segundos = sec % 3600
minutes = segundos // 60
segundosfinais = segundos % 60
print(f"{sec} tem {h} Horas, {minutes} Minutos e {segundosfinais} Segundos.")