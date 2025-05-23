menor = None

numero = int(input("Digite um número (-1 para parar): "))

while numero != -1:
    if menor is None or numero < menor:
        menor = numero
    numero = int(input("Digite outro número (-1 para parar): "))

if menor is not None:
    print(f"O menor número digitado foi: {menor}")
else:
    print("Nenhum número válido foi digitado.")
