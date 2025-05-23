def contar_impares(lista):
    contador = 0
    for num in lista:
        if num % 2 != 0:
            contador += 1
    return contador

print(contar_impares([1, 2, 3, 4, 5, 6]))  # 3