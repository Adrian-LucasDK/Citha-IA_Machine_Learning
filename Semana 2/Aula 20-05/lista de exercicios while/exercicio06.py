numero = int(input("Digite um número positivo: "))

while numero < 0:
    print("Número negativo! Tente novamente.")
    numero = int(input("Digite um número positivo: "))

print(f"Você digitou o número positivo: {numero}")
