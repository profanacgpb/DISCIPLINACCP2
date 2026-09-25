from time import sleep

vermelho, branco, verde, fim = "\033[31m", "\033[37m", "\033[32m", "\033[0m"
caminho_arquivo = "Repositórios-Públicos/DISCIPLINACCP2/Gabriel-Porto/Python-Estrutura-de-Dados/Arquivos/Questão-01-a-10/mini-sistema.txt"

palavara_inicializacao = str(input("Digite a palavra chave (MINI-SISTEMA) para prosseguir: "))

while (palavara_inicializacao != "MINI-SISTEMA"):
    if palavara_inicializacao != "MINI-SISTEMA":
        print(f"{vermelho}Você digitou {branco}{palavara_inicializacao}{fim}{vermelho}, verifique a ortografia e tente novamente{fim}")
        palavara_inicializacao = str(input("Digite a palavra chave (MINI-SISTEMA) novamente para prosseguir: "))
    else:
        continue
while (palavara_inicializacao == "MINI-SISTEMA"):
    print ("\n")
    print("-=-"*10)
    print("     (1) - CADASTRAR ALUNO")
    print("     (2) - LISTAR ALUNOS")
    print("     (3) - SAIR")
    print("-=-"*10 + "\n")
    opcao_usuario = int(input("Escolha uma opção acima: "))

    while (opcao_usuario != 1 or opcao_usuario != 2 or opcao_usuario != 3):
        if (opcao_usuario) == 1:
            arquivo = open(caminho_arquivo, "w")
            quantidade_cadastro = int(input("Digite a quantidade de alunos que você quer cadastrar: "))
            if quantidade_cadastro > 0:
                for indice in range(1, quantidade_cadastro+1, +1):
                    nome_aluno = input(f"Digite o nome do aluno ({indice}): ")
                    arquivo.write(nome_aluno + "\n")
                print(f"{verde}Alunos cadastrados com sucesso!!!{fim}")    
            else:
                print(f"{vermelho}Por favor verifique o número digitado e tente novamente, você digitou {quantidade_cadastro}{fim}")
            arquivo.close()
            break
        
        elif (opcao_usuario) == 2:
            arquivo = open(caminho_arquivo, "r")
            exibicao_aluno = arquivo.read()
            print(exibicao_aluno)
            arquivo.close()
            print(f"{verde}Alunos Listados!!!{fim}")
            break

        elif (opcao_usuario) == 3:
            print("Finalizando o Programa...")
            for time_break in range(5,0,-1):
                print(time_break)
                sleep(1)
            print(f"{verde}Programa Finalizado com êxito.{fim}")    
            break

        else:
            print(f"{vermelho}Você digitou {branco}{opcao_usuario}{fim}{vermelho}, verifique e tente novamente{fim}")
            opcao_usuario = int(input("Escolha uma opção acima (novamente): "))
    break