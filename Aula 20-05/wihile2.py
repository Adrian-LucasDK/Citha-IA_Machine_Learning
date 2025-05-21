numero = int(input("Digite um número inteiro (0 para sair): "))

while numero != 0:
    print(f"\nTabuada do {numero}:")
    i = 1
    while i <= 10:
        print(f"{numero} x {i} = {numero * i}")
        i += 1
    print()  # linha em branco para separar visualmente
    numero = int(input("Digite outro número inteiro (0 para sair): "))

print("Programa encerrado.")