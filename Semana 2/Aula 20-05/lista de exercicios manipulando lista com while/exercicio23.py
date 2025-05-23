numeros_positivos = []

while True:
    num = float(input("Digite um número (digite 0 para parar): "))
    if num == 0:
        break
    if num > 0:
        numeros_positivos.append(num)

print("Números positivos digitados:", numeros_positivos)
