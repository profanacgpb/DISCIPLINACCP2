# Crie uma tabuada completa de 1 a 10 usando dois loops.

for x in range (1,11):
    print(f"\nTabuada do {x}")

    for y in range(1,11):
        resultado = x * y
        print(f"{x} x {y} = {resultado}")