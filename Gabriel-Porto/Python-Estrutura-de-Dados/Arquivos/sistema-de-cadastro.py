caminho_arquivo =  "/home/gabriel_porto/Documentos/Repositórios GitHub/Repositórios-Públicos/DISCIPLINACCP2/Gabriel-Porto/Python-Estrutura-de-Dados/Arquivos/sistema-de-cadastro.txt"


dados = {
    "nome": "Gabriel",
    "idade": 19,
    "curso": "Ciência-Computação"
}

with open (caminho_arquivo, "a") as arquivo:
    for chave, valor in dados.items():
        arquivo.write (str(f"{chave}: {valor}") + "\n")