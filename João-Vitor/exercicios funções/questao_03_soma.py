def somar(a, b):
    """Retorna a soma de dois números."""
    return a + b


if __name__ == "__main__":
    primeiro_numero = float(input("Primeiro número: "))
    segundo_numero = float(input("Segundo número: "))
    resultado = somar(primeiro_numero, segundo_numero)
    print(f"Resultado: {resultado:g}")
