print("------Tabuada------")
num = int(input("Digite um número: "))

print("-"*12)
for i in range(1,11):
    tabu = num * i
    print(f"{num} x {i} = {tabu}")
print("-"*12)