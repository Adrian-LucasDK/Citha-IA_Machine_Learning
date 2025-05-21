numero = int(input("Digite um número para ver seus divisores: "))

divisor = 1

print(f"Divisores de {numero}:")

while divisor <= numero:
    if numero % divisor == 0:
        print(divisor)
    divisor += 1
