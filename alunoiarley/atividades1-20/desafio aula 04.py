segundos = int(input("digite o tempo em segundos: "))
horas = segundos // 3600
resto = segundos % 3600
minutos = resto // 60
segundos = resto % 60

print(f"o tempo em horas é: {horas}h, minutos: {minutos}m e segundos: {segundos}s")