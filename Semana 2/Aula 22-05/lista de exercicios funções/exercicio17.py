def positivos(lista):
    positivos_lista = []
    for valor in lista:
        if valor > 0:
            positivos_lista.append(valor)
    return positivos_lista

print(positivos([-1, 2, -3, 4, -5, 6]))