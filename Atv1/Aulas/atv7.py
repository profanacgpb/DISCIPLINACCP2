nome=(input("Digite seu nome: "))
n1=int(input("Digite sua primeira nota: "))
n2=int(input("Digite sua segunda nota: "))

media=(n1+n2)/2

if media>= 7 :
    print(f"{nome}, está aprovado. Sua média foi: {media}")
else :
    print(f"{nome}, está reprovado. Sua média foi: {media}")
