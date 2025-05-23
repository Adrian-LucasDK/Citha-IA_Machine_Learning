numero = 1
contador_impares = 0

while numero <= 50:
    if numero % 2 != 0:
        contador_impares += 1
    numero += 1

print(f"Quantidade de números ímpares entre 1 e 50: {contador_impares}")
