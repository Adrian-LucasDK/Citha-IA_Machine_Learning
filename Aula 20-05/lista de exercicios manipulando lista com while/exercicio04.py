numeros = [3, 6, 9, 11, 14, 17, 19]

contador_impares = 0
i = 0

while i < len(numeros):
    if numeros[i] % 2 != 0:
        contador_impares += 1
    i += 1

print(f"Quantidade de números ímpares na lista: {contador_impares}")
