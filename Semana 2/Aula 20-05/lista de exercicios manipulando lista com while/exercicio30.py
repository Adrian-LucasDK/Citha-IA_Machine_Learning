lista = [9, 4, 6, 2, 8]

n = len(lista)
troca = True

while troca:
    troca = False
    i = 0
    while i < n - 1:
        if lista[i] > lista[i + 1]:
            # troca os elementos
            lista[i], lista[i + 1] = lista[i + 1], lista[i]
            troca = True
        i += 1
    n -= 1  # otimização: a cada passagem, o maior elemento fica no final

print("Lista ordenada:", lista)
