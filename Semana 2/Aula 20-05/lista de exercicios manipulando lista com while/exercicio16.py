lista = [3, 6, 9, 12, 15, 18, 21]

i = 0

while i < len(lista):
    if lista[i] % 3 == 0:
        print(f"O número {lista[i]} está no índice {i}")
    i += 1
