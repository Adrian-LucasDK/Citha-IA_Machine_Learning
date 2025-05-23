def multiplicar(lista, n):
    nova_lista = []
    for item in lista:
        nova_lista.append(item * n)
    return nova_lista

print(multiplicar([1, 2, 3, 4], 2))