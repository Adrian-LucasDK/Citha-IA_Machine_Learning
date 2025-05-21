notas = [7.5, 8.0, 6.5, 9.0, 5.5]

soma = 0
i = 0

while i < len(notas):
    soma += notas[i]
    i += 1

media = soma / len(notas)
print(f"A média das notas é: {media:.2f}")
