numeros = [1, 4, 7, 10, 13, 16, 19, 22]
contador = 0

for num in numeros:
    if num % 2 != 0:
        contador += 1

print("Quantidade de números ímpares:", contador)
