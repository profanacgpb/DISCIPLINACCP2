def ler_notas():
    notas = []
    while len(notas) < 3:
        try:
            nota = float(input(f"Digite a {len(notas) + 1}ª nota: ").replace(",", "."))
            if 0 <= nota <= 10:
                notas.append(nota)
            else:
                print("A nota deve estar entre 0 e 10.")
        except ValueError:
            print("Digite uma nota válida.")
    return notas


def calcular_media(notas):
    return sum(notas) / len(notas)


def verificar_situacao(media):
    if media >= 7:
        return "Aprovado"
    return "Reprovado"


def exibir_resultado(media, situacao):
    print(f"\nMédia final: {media:.2f}")
    print(f"Situação: {situacao}")


if __name__ == "__main__":
    print("Sistema de notas")
    print("A média mínima para aprovação é 7.")
    notas = ler_notas()
    media = calcular_media(notas)
    situacao = verificar_situacao(media)
    exibir_resultado(media, situacao)
