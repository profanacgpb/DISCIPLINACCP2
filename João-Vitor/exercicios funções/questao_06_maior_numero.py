def maior_numero(a, b, c):
    """Retorna o maior valor sem utilizar max()."""
    maior = a
    if b > maior:
        maior = b
    if c > maior:
        maior = c
    return maior


if __name__ == "__main__":
    primeiro_numero = float(input("Primeiro número: "))
    segundo_numero = float(input("Segundo número: "))
    terceiro_numero = float(input("Terceiro número: "))
    resultado = maior_numero(primeiro_numero, segundo_numero, terceiro_numero)
    print(f"Maior número: {resultado:g}")
