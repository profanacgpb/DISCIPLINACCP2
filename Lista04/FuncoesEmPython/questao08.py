def celsius_para_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_para_celsius(fahrenheit):
    return (fahrenheit - 32) * (5/9)

print("========== CONVERSOR ==========")

c = float(input("Digite o valor a ser convertido em Fahrenheit: "))
f = float(input("Digite o valor a ser convertido em celsius: "))

conv_c = fahrenheit_para_celsius(f)
conv_f = celsius_para_fahrenheit(c)

print(f"O valor convertido de Fahrenheit para Celsius é {conv_c:.2f}")
print(f"O valor convertido de Celsius para Fahrenheit é {conv_f:.2f}")