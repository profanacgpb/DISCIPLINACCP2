#Faça um programa que receba uma quantidade de segundos e converta para horas, minutos e segundos.
print("-----------------COVERSOR---------------")
segundos = int(input("Digite a quantidade de segundos: "))

horas = segundos // 3600
segundos_restantes = segundos % 3600

minutos = segundos_restantes // 60
segundos_finais = segundos_restantes % 60

print(f"{horas} hora(s), {minutos} minuto(s) e {segundos_finais} segundo(s)")