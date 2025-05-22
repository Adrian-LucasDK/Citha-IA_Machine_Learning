numeros = [1, 2, 2, 3, 3, 3, 4]

lista_unica = []
i = 0

while i < len(numeros):
    if numeros[i] not in lista_unica:
        lista_unica.append(numeros[i])
    i += 1

print("Lista sem duplicados:", lista_unica)
