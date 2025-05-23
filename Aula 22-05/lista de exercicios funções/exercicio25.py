def eh_multiplo(n1, n2):
    if n2 == 0:
        return False  # Evita divisão por zero
    return n1 % n2 == 0

print(eh_multiplo(10, 2))  # Saída: True