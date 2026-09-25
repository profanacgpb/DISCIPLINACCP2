print("========== CONVERSOR ==========")
print("1 - Celsius → Fahrenheit")
print("2 - Fahrenheit → Celsius")

escolha = int(input("Escolha uma opção acima: "))

if escolha ==1:
    celsius = float(input("Digite a temperatura em Celsius: "))
    fahrenheit = (celsius * 9/5) + 32
    print(f"{celsius}°C é igual a {fahrenheit}°F")
else:
    fahrenheit = float(input("Digite a temperatura em Fahrenheit: "))
    celsius = (fahrenheit - 32) * 5/9
    print(f"{fahrenheit}°F é igual a {celsius}°C")