def celsius_para_fahrenheit(celsius):
    return celsius * 9 / 5 + 32


def fahrenheit_para_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9


def ler_temperatura(mensagem):
    while True:
        try:
            return float(input(mensagem))
        except ValueError:
            print("Digite uma temperatura válida.")


def menu():
    while True:
        print("\n========== CONVERSOR ==========")
        print("1 - Celsius → Fahrenheit\n2 - Fahrenheit → Celsius\n3 - Sair")
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "3":
            print("Conversor encerrado.")
            break
        if opcao == "1":
            celsius = ler_temperatura("Temperatura em Celsius: ")
            print(f"Resultado: {celsius_para_fahrenheit(celsius):.1f} °F")
        elif opcao == "2":
            fahrenheit = ler_temperatura("Temperatura em Fahrenheit: ")
            print(f"Resultado: {fahrenheit_para_celsius(fahrenheit):.1f} °C")
        else:
            print("Opção inválida.")


if __name__ == "__main__":
    menu()
