def saudacao(nome):
    return f"Olá,{nome}! Bem-vindo à disciplina de Programação."

nome = input("Digite seu nome: ")
mensagem = saudacao(nome)
print(mensagem)