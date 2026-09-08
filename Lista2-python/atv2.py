notas = [7.5, 8.0, 6.5, 9.0, 5.5]

maior = max(notas)

menor = min(notas)

quantidade = len(notas)

soma = sum(notas)

media = soma / quantidade

ordenadas = sorted(notas)

tres_maiores = sorted(notas, reverse=True)[:3]

print(f"Maior nota: {maior}")
print(f"Menor nota: {menor}")
print(f"Quantidade: {quantidade}")
print(f"Soma: {soma}")
print(f"Média: {media}")
print(f"Notas ordenadas: {ordenadas}")
print(f"3 maiores notas: {tres_maiores}")