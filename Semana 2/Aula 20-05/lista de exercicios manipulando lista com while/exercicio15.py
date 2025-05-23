valores = [40, 10, 85, 60, 20]

i = 0
maior = valores[0]  # Assume o primeiro como maior inicialmente

while i < len(valores):
    if valores[i] > maior:
        maior = valores[i]
    i += 1

print(f"O maior valor da lista é: {maior}")
