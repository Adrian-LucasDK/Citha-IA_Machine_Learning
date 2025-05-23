contador_maiores = 0

idade = int(input("Digite a idade (ou -1 para encerrar): "))

while idade != -1:
    if idade >= 18:
        contador_maiores += 1
    idade = int(input("Digite a idade (ou -1 para encerrar): "))

print(f"Quantidade de pessoas maiores de idade: {contador_maiores}")
