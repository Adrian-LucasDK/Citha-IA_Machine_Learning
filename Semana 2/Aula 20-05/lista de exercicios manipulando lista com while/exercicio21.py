lista1 = [1, 2, 3]
lista2 = [4, 5, 6]

i = 0
while i < len(lista1) and i < len(lista2):
    soma = lista1[i] + lista2[i]
    print(f"Soma dos elementos na posição {i}: {lista1[i]} + {lista2[i]} = {soma}")
    i += 1
