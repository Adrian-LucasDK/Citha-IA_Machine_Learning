numeros = [1, 2, 3, 4, 5]

produto = 1
i = 0

while i < len(numeros):
    produto *= numeros[i]
    i += 1

print(f"O produto de todos os elementos é: {produto}")
