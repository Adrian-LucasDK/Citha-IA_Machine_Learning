def soma_pares(lista):
    soma = 0
    for num in lista:
        if num % 2 == 0:
            soma += num
    return soma

print(soma_pares([1, 2, 3, 4, 5, 6]))