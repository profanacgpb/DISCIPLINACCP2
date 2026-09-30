def ler_numero(mensagem, tipo=float):
    while True:
        try:
            return tipo(input(mensagem))
        except ValueError:
            print("Valor inválido. Tente novamente.")


def calcular_media(aluno):
    return (aluno["nota_1"] + aluno["nota_2"] + aluno["nota_3"]) / 3


def verificar_situacao(media):
    if media >= 7:
        return "Aprovado"
    if media >= 5:
        return "Recuperação"
    return "Reprovado"


def cadastrar_aluno(alunos):
    aluno = {
        "nome": input("Nome: ").strip(),
        "idade": ler_numero("Idade: ", int),
        "curso": input("Curso: ").strip(),
        "nota_1": ler_numero("Nota 1: "),
        "nota_2": ler_numero("Nota 2: "),
        "nota_3": ler_numero("Nota 3: "),
    }
    alunos.append(aluno)
    print("Aluno cadastrado com sucesso.")


def exibir_aluno(aluno):
    media = calcular_media(aluno)
    print(
        f"Nome: {aluno['nome']} | Idade: {aluno['idade']} | Curso: {aluno['curso']}\n"
        f"Notas: {aluno['nota_1']:.1f}, {aluno['nota_2']:.1f}, {aluno['nota_3']:.1f}\n"
        f"Média: {media:.1f} | Situação: {verificar_situacao(media)}"
    )


def listar_alunos(alunos):
    if not alunos:
        print("Nenhum aluno cadastrado.")
        return
    for aluno in alunos:
        exibir_aluno(aluno)
        print("-" * 40)


def buscar_aluno(alunos):
    termo = input("Nome para buscar: ").strip().casefold()
    encontrados = [aluno for aluno in alunos if termo in aluno["nome"].casefold()]
    if not encontrados:
        print("Aluno não encontrado.")
        return
    for aluno in encontrados:
        exibir_aluno(aluno)


def mostrar_medias(alunos):
    if not alunos:
        print("Nenhum aluno cadastrado.")
        return
    for aluno in alunos:
        print(f"{aluno['nome']}: {calcular_media(aluno):.1f}")


def mostrar_situacoes(alunos):
    if not alunos:
        print("Nenhum aluno cadastrado.")
        return
    for aluno in alunos:
        situacao = verificar_situacao(calcular_media(aluno))
        print(f"{aluno['nome']}: {situacao}")


def remover_aluno(alunos):
    nome = input("Nome exato do aluno a remover: ").strip().casefold()
    for aluno in alunos:
        if aluno["nome"].casefold() == nome:
            alunos.remove(aluno)
            print("Aluno removido com sucesso.")
            return
    print("Aluno não encontrado.")


def alterar_dados(alunos):
    nome = input("Nome exato do aluno a alterar: ").strip().casefold()
    for aluno in alunos:
        if aluno["nome"].casefold() == nome:
            aluno["idade"] = ler_numero("Nova idade: ", int)
            aluno["curso"] = input("Novo curso: ").strip()
            aluno["nota_1"] = ler_numero("Nova nota 1: ")
            aluno["nota_2"] = ler_numero("Nova nota 2: ")
            aluno["nota_3"] = ler_numero("Nova nota 3: ")
            print("Dados atualizados com sucesso.")
            return
    print("Aluno não encontrado.")


def mostrar_maior_media(alunos):
    if not alunos:
        print("Nenhum aluno cadastrado.")
        return
    maior_media = max(calcular_media(aluno) for aluno in alunos)
    print(f"Maior média da turma: {maior_media:.1f}")
    for aluno in alunos:
        if calcular_media(aluno) == maior_media:
            exibir_aluno(aluno)


def mostrar_media_geral(alunos):
    if not alunos:
        print("Nenhum aluno cadastrado.")
        return
    media_geral = sum(calcular_media(aluno) for aluno in alunos) / len(alunos)
    print(f"Média geral da turma: {media_geral:.1f}")


def menu():
    alunos = []
    acoes = {
        "1": lambda: cadastrar_aluno(alunos),
        "2": lambda: listar_alunos(alunos),
        "3": lambda: mostrar_medias(alunos),
        "4": lambda: mostrar_situacoes(alunos),
        "5": lambda: buscar_aluno(alunos),
        "7": lambda: remover_aluno(alunos),
        "8": lambda: alterar_dados(alunos),
        "9": lambda: mostrar_maior_media(alunos),
        "10": lambda: mostrar_media_geral(alunos),
    }
    while True:
        print("\n========== SISTEMA ACADÊMICO ==========")
        print("1-Cadastrar  2-Listar  3-Calcular média  4-Verificar situação")
        print("5-Buscar  6-Sair  7-Remover  8-Alterar  9-Maior média  10-Média geral")
        opcao = input("Escolha uma opção: ").strip()
        if opcao == "6":
            print("Sistema encerrado.")
            break
        if opcao in acoes:
            acoes[opcao]()
        else:
            print("Opção inválida.")


if __name__ == "__main__":
    menu()
