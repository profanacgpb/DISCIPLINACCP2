def celsius_para_fahrenheit(celsius):
    return(celsius * 9 / 5) + 32

def fahrenheit_para_celsius(fahrenheit):
    return (fahrenheit -32) * 5 / 9

while True:
    print("======Conversor =======")
    print("1 - Celsius > Fehrenheit")
    print("2 - Fehrenheit > Celsius")
    print("3 - Sair")
    
    opcao = input("Escolha uma opção:")
    
    if opcao == "1":
        celsius = float(input("Digite  a temperatura em Celsius:"))
        resultado = celsius_para_fahrenheit(celsius)
        print(f"{celsius} °C = {resultado:.2f} °F")
    elif opcao == "2":
        fahrenheit = float(input("Digite a temperatura em Fehrenheit:"))
        resultado = fahrenheit_para_celsius(fahrenheit)
        print(f"{fahrenheit} °F = {resultado:.2f} °C")
    elif opcao == "3":
        print("Conversão encerrado.")
        break
    
    else:
        print("Opção inválida. Tente novamente.")
    