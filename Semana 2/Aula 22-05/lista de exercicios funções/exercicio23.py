def verificar_numero(n):
    if n > 0:
        return 'Positivo'
    elif n < 0:
        return 'Negativo'
    else:
        return 'Zero'

print(verificar_numero(10))  # Saída: Positivo