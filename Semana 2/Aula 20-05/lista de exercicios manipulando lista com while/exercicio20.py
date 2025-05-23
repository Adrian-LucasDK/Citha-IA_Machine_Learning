lista = ['A', 'B', 'C', 'D', 'E', 'F']

i = 0

print("Elementos nas posições ímpares:")
while i < len(lista):
    if i % 2 != 0:
        print(f"Índice {i}: {lista[i]}")
    i += 1
