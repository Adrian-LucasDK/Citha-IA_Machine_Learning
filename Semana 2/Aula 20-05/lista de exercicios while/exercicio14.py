numero = int(input("Digite um número para calcular o fatorial: "))

fatorial = 1
contador = numero

while contador > 0:
    fatorial *= contador
    contador -= 1

print(f"O fatorial de {numero} é {fatorial}")
