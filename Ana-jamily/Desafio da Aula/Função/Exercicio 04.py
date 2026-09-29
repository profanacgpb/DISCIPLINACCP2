n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))
n3 = float(input("Digite a terceira nota: "))

def calcular_media(n1, n2, n3):
    return (n1 + n2 + n3) / 3

resultado = calcular_media(n1, n2, n3)

print("A media e:", resultado)