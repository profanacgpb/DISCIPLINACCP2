def maior(a, b):
    if a >= b:
        return a
    return b


if __name__ == "__main__":
    try:
        a = float(input("Digite o primeiro número: ").replace(",", "."))
        b = float(input("Digite o segundo número: ").replace(",", "."))
        print(f"Maior número: {maior(a, b):g}")
    except ValueError:
        print("Digite apenas valores numéricos.")
