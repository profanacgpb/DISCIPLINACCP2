def saudacao(nome):
    print(f"Olá, {nome}! Seja bem-vindo!")


if __name__ == "__main__":
    nome = input("Digite seu nome: ").strip()
    saudacao(nome)
