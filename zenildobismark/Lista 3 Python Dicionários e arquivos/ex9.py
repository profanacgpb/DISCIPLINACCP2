# Crie um arquivo chamado alunos.txt e escreva nele os nomes de 5 alunos.
arquivo = open('alunos.txt', 'w')

arquivo.write('Zenildo\n')
arquivo.write('Bismark\n')
arquivo.write('Rodrigues\n')
arquivo.write('da\n')
arquivo.write('Luz\n')

arquivo.close()