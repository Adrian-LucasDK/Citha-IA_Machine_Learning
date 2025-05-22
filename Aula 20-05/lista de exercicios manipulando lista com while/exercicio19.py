numeros = [7, 3, 7, 1, 7, 9]

i = 0
contador = 0

while i < len(numeros):
    if numeros[i] == 7:
        contador += 1
    i += 1

print(f"O número 7 aparece {contador} vezes na lista.")
