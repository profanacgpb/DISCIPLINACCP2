def calcular_media(n1, n2, n3):
    return (n1 + n2 + n3) / 3


if __name__ == "__main__":
    try:
        n1 = float(input("Digite a primeira nota: ").replace(",", "."))
        n2 = float(input("Digite a segunda nota: ").replace(",", "."))
        n3 = float(input("Digite a terceira nota: ").replace(",", "."))
        media = calcular_media(n1, n2, n3)
        print(f"Média: {media:.2f}")
    except ValueError:
        print("Digite apenas valores numéricos para as notas.")
