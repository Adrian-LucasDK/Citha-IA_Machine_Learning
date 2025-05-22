letras = ['a', 'b', 'c', 'd', 'e']
invertida = []

i = len(letras) - 1

while i >= 0:
    invertida.append(letras[i])
    i -= 1

print("Lista original:", letras)
print("Lista invertida:", invertida)
