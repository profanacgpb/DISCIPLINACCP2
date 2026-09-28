#Questão 8- Lista de compras
produto1 = input("Seu produto é ")
produto2 = input("Seu produto é ")
produto3 = input("Seu produto é ")
produto4 = input("Seu produto é ")
produto5 = input("Seu produto é ")
with open("Lista_produtos", "w")as Lista_produtos:
   Lista_produtos.write(produto1+"\n")
   Lista_produtos.write(produto2+"\n")
   Lista_produtos.write(produto3+"\n")
   Lista_produtos.write(produto4+"\n")
   Lista_produtos.write(produto5+"\n")
with open("Lista_produtos", "r")as Lista_produtos:
  print(Lista_produtos.read())
