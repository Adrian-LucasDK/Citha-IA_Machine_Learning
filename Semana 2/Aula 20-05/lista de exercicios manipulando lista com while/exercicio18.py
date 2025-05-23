numeros = [2, 5, 6, 9, 10]

i = 0

while i < len(numeros):
    if numeros[i] % 2 == 0:
        numeros[i] = 0
    i += 1

print("Lista após substituir pares por 0:", numeros)
