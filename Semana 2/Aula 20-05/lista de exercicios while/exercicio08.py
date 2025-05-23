maior = None

numero = int(input("Digite um número (0 para sair): "))

while numero != 0:
    if (maior is None) or (numero > maior):
        maior = numero
    numero = int(input("Digite outro número (0 para sair): "))

if maior is not None:
    print(f"O maior número digitado foi: {maior}")
else:
    print("Nenhum número válido foi digitado.")
