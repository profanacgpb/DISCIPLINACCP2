arquivo=open("alunos.txt", "r")

for nome in arquivo:
    print("aluno: ", nome.strip())
    
arquivo.close()