lista1 = [1, 2, 3]
lista2 = [4, 5, 6]

somas = []
i = 0

while i < len(lista1) and i < len(lista2):
    soma = lista1[i] + lista2[i]
    somas.append(soma)
    i += 1

print("Lista com a soma dos elementos correspondentes:", somas)
