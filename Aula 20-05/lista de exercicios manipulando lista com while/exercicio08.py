numeros = [10, -5, 8, -2, 15, -1]

i = 0
while i < len(numeros):
    if numeros[i] < 0:
        numeros.pop(i)
        # Não incrementa i porque a lista "anda" para trás após pop
    else:
        i += 1

print("Lista após remover negativos:", numeros)
