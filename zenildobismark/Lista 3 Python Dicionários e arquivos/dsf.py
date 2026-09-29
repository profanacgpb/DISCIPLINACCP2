import json
import os

ARQUIVO = 'alunos.json'

# Dados iniciais para preencher o arquivo caso ele ainda não exista
ALUNOS_INICIAIS = [
    {'nome': 'Zenildo', 'idade': 26, 'curso': 'Ciência da Computação', 'nota': 9.0},
    {'nome': 'Maria', 'idade': 22, 'curso': 'Administração', 'nota': 8.5},
    {'nome': 'João', 'idade': 25, 'curso': 'Engenharia', 'nota': 7.5},
    {'nome': 'Pedro', 'idade': 21, 'curso': 'Sistemas de Informação', 'nota': 8.0},
    {'nome': 'Ana', 'idade': 23, 'curso': 'Direito', 'nota': 9.5}
]

def carregar_alunos():
    """Lê os alunos do arquivo JSON. Se não existir, salva os dados iniciais."""
    if not os.path.exists(ARQUIVO):
        salvar_alunos(ALUNOS_INICIAIS)
        return ALUNOS_INICIAIS
    
    try:
        with open(ARQUIVO, 'r', encoding='utf-8') as f:
            return json.load(f)
    except Exception:
        return []

def salvar_alunos(alunos):
    """Salva a lista completa de alunos no arquivo JSON."""
    with open(ARQUIVO, 'w', encoding='utf-8') as f:
        json.dump(alunos, f, indent=4, ensure_ascii=False)

def cadastrar_aluno(alunos):
    print("\n--- Cadastrar Aluno ---")
    nome = input("Nome: ").strip()
    idade = int(input("Idade: "))
    curso = input("Curso: ").strip()
    nota = float(input("Nota: "))

    novo_aluno = {
        "nome": nome,
        "idade": idade,
        "curso": curso,
        "nota": nota
    }
    
    alunos.append(novo_aluno)
    salvar_alunos(alunos)
    print(f"Aluno(a) {nome} cadastrado(a) com sucesso!")

def listar_alunos(alunos):
    print("\n--- Lista de Alunos ---")
    if not alunos:
        print("Nenhum aluno cadastrado.")
        return

    for i, aluno in enumerate(alunos, start=1):
        print(f"{i}. Nome: {aluno['nome']} | Idade: {aluno['idade']} | Curso: {aluno['curso']} | Nota: {aluno['nota']}")

def pesquisar_aluno(alunos):
    print("\n--- Pesquisar Aluno ---")
    nome_busca = input("Digite o nome do aluno: ").strip().lower()
    encontrados = [a for a in alunos if nome_busca in a['nome'].lower()]

    if encontrados:
        for aluno in encontrados:
            print(f"Nome: {aluno['nome']} | Idade: {aluno['idade']} | Curso: {aluno['curso']} | Nota: {aluno['nota']}")
    else:
        print("Nenhum aluno encontrado com esse nome.")

def alterar_aluno(alunos):
    print("\n--- Alterar Aluno ---")
    nome_busca = input("Digite o nome do aluno que deseja alterar: ").strip().lower()
    
    for aluno in alunos:
        if aluno['nome'].lower() == nome_busca:
            print(f"Aluno encontrado: {aluno['nome']}")
            aluno['idade'] = int(input(f"Nova idade (Atual: {aluno['idade']}): "))
            aluno['curso'] = input(f"Novo curso (Atual: {aluno['curso']}): ").strip()
            aluno['nota'] = float(input(f"Nova nota (Atual: {aluno['nota']}): "))
            
            salvar_alunos(alunos)
            print("Dados atualizados com sucesso!")
            return

    print("Aluno não encontrado.")

def remover_aluno(alunos):
    print("\n--- Remover Aluno ---")
    nome_busca = input("Digite o nome do aluno que deseja remover: ").strip().lower()
    
    for i, aluno in enumerate(alunos):
        if aluno['nome'].lower() == nome_busca:
            aluno_removido = alunos.pop(i)
            salvar_alunos(alunos)
            print(f"Aluno(a) {aluno_removido['nome']} removido(a) com sucesso!")
            return

    print("Aluno não encontrado.")

# Loop principal da aplicação
def main():
    alunos = carregar_alunos()

    while True:
        print("\n" + "=" * 32 + " SISTEMA DE ALUNOS " + "=" * 33)
        print("1 - Cadastrar aluno")
        print("2 - Listar alunos")
        print("3 - Pesquisar aluno")
        print("4 - Alterar aluno")
        print("5 - Remover aluno")
        print("6 - Sair")

        opcao = input("Digite a opção desejada: ").strip()

        if opcao == '1':
            cadastrar_aluno(alunos)
        elif opcao == '2':
            listar_alunos(alunos)
        elif opcao == '3':
            pesquisar_aluno(alunos)
        elif opcao == '4':
            alterar_aluno(alunos)
        elif opcao == '5':
            remover_aluno(alunos)
        elif opcao == '6':
            print("Encerrando o programa...")
            break
        else:
            print("Opção inválida! Tente novamente.")

if __name__ == "__main__":
    main()
