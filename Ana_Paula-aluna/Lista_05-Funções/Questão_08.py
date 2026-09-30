#QUESTÃO 08 — Conversão de temperatura
#Crie celsius_para_fahrenheit(celsius) e fahrenheit_para_celsius(fahrenheit). Use F = (C × 9/5) + 32 e C = (F - 32) × 5/9. Crie um menu.

def celsius_para_fahrenheit(celsius):
    temp_fahrenheit = (celsius * (9/5)) + 32
    return temp_fahrenheit

def fahrenheit_para_celsius(fahrenheit):
    temp_celsius = (fahrenheit - 32) * (5/9)
    return temp_celsius

print("========== CONVERSOR ==========")
print(" 1 - Celsius para Fahrenheit")
print(" 2 - Fahrenheit para Celsius")
print(" 3 - Sair")

opcao = int(input("Escolha uma opção: "))

while True:
    if opcao == 1:
        temp_C = float(input("Temperatura em Celsius: "))
        temp_F = celsius_para_fahrenheit(temp_C)
        print(f"{temp_C} Celsius = {temp_F:.1f} Fahrenheit")

    elif opcao == 2:
        temp_F = float(input("Temperatura em Fahrenheit: "))
        temp_C = fahrenheit_para_celsius(temp_F)
        print(f"{temp_F} Fahrenheit = {temp_C:.1f} Celsius")

    elif opcao == 3:
        break

    else:
        print("Opção Inválida!")
        
    opcao = int(input("\nEscolha uma opção: "))

print("\n- Fim do programa -")
