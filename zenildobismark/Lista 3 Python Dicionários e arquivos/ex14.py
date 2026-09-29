# Crie mensagem.txt, escreva “Primeira mensagem” e depois, usando o modo w, 
# substitua por “Nova mensagem”. Leia o arquivo e verifique o resultado.
with open('mensagem.txt', 'w') as arquivo:
    arquivo.write('Primeira mensagem')

with open('mensagem.txt', 'w') as arquivo:
    arquivo.write('Nova mensagem')

with open('mensagem.txt', 'r') as arquivo:
    mensagem = arquivo.read()
    print(mensagem.strip())