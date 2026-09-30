def saudacao(nome):
    """Retorna uma saudação personalizada."""
    return f"Olá, {nome}! Seja bem-vinda à programação."


if __name__ == "__main__":
    nome = input("Digite seu nome: ").strip()
    print(saudacao(nome))
