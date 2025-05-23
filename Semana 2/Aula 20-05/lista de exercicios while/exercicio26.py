soma = 0
contador = 0

while True:
    numero = float(input("Digite um número: "))
    soma += numero
    contador += 1
    media = soma / contador

    print(f"Média atual: {media:.2f}")

    if media > 7:
        break

print("Média maior que 7 alcançada. Programa encerrado.")
