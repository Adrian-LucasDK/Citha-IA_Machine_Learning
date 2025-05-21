contador_pares = 0

numero = int(input("Digite um número (-1 para parar): "))

while numero != -1:
    if numero % 2 == 0:
        contador_pares += 1
    numero = int(input("Digite outro número (-1 para parar): "))

print(f"Quantidade de números pares digitados: {contador_pares}")
