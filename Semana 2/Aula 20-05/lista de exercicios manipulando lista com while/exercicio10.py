numeros = []
soma = 0

while soma <= 100:
    num = float(input("Digite um número: "))
    numeros.append(num)
    soma += num

print(f"Soma total: {soma}")
print("Números digitados:", numeros)
