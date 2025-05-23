contador_negativos = 0

numero = int(input("Digite um número (999 para encerrar): "))

while numero != 999:
    if numero < 0:
        contador_negativos += 1
    numero = int(input("Digite outro número (999 para encerrar): "))

print(f"Você digitou {contador_negativos} números negativos.")
