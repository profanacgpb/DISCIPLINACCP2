def dados_da_pessoa():
    nome = input("Nome: ")
    idade = input("Idade: ")
    curso = input("Curso: ")
    return {"Nome": nome, "Idade": idade, "Curso": curso}


def salvar_cadastros(lista_pessoas, arquivo="cadastros.txt"):
        for pessoa in lista_pessoas:
            linha = f"Nome: {pessoa['Nome']}\nIdade: {pessoa['Idade']}\nCurso: {pessoa['Curso']}\n"
            with open(arquivo, "a", encoding="utf-8") as f:
                f.write(linha)


def main():
    cadastros = [] 
    while True:
        pessoa = dados_da_pessoa()
        cadastros.append(pessoa)

        continuar = input("Cadastrar outra pessoa? (s/n): ").strip().lower()
        if continuar != "s":
            break

    salvar_cadastros(cadastros)
    print(f"\n{len(cadastros)} cadastro(s) salvo(s) com sucesso em 'cadastros.txt'!")


if __name__ == "__main__":
    main() 