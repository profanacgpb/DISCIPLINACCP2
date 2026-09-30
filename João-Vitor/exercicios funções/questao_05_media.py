def calcular_media(n1, n2, n3):
    """Calcula a média aritmética de três notas."""
    return (n1 + n2 + n3) / 3


def verificar_situacao(media):
    """Retorna a situação do aluno conforme a média recebida."""
    if media >= 7:
        return "Aprovado"
    if media >= 5:
        return "Recuperação"
    return "Reprovado"


if __name__ == "__main__":
    nome = input("Aluno: ").strip()
    nota_1 = float(input("Nota 1: "))
    nota_2 = float(input("Nota 2: "))
    nota_3 = float(input("Nota 3: "))
    media = calcular_media(nota_1, nota_2, nota_3)

    print(f"\nAluno: {nome}")
    print(f"Média: {media:.1f}")
    print(f"Situação: {verificar_situacao(media)}")
