#Crie celsius_para_fahrenheit(celsius) e fahrenheit_para_celsius(fahrenheit). 
# Use F = (C × 9/5) + 32 e C = (F - 32) × 5/9. Crie um menu.

def celsius_para_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_para_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

while True:
    print("\n=== CONVERSOR DE TEMPERATURA ===")
    print("1 - Converter Celsius para Fahrenheit")
    print("2 - Converter Fahrenheit para Celsius")
    print("3 - Sair")
    
    opcao = input("Escolha uma opção (1-3): ").strip()

    if opcao == '1':
        c = float(input("Digite a temperatura em °C: "))
        f = celsius_para_fahrenheit(c)
        print(f"-> {c}°C equivale a {f:.2f}°F")

    elif opcao == '2':
        f = float(input("Digite a temperatura em °F: "))
        c = fahrenheit_para_celsius(f)
        print(f"-> {f}°F equivale a {c:.2f}°C")

    elif opcao == '3':
        print("Encerrando o programa... Até logo!")
        break

    else:
        print("Opção inválida! Digite 1, 2 ou 3.")