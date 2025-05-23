numeros = [3, 8, 12, 25, 30]

i = 0
encontrado = False

while i < len(numeros):
    if numeros[i] == 25:
        encontrado = True
        break
    i += 1

if encontrado:
    print("O número 25 está na lista.")
else:
    print("O número 25 não está na lista.")
