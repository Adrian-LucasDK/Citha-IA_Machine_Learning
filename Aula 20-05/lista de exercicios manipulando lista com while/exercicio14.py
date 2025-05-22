numeros = [5, 12, 7, 18, 3, 11]

contador = 0
i = 0

while i < len(numeros):
    if numeros[i] > 10:
        contador += 1
    i += 1

print(f"Quantidade de números maiores que 10: {contador}")
