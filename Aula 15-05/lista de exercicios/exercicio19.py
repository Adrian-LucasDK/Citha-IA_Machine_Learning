pont = int(input("Digite um a sua pontuação no intervalo de 0-100: "))

if pont < 0 or pont > 100:
    print("Operação Inválida! Digite um número no intervalo de 0-100")
elif pont < 50:
    print(f"Sua pontuação de {pont} é considerada ruim")
elif pont >= 50 and pont <= 70:
    print(f"Sua pontuação de {pont} é considerada regular")
elif pont >= 71 and pont <= 90:
    print(f"Sua pontuação de {pont} é considerada boa")
else:
    print(f"Sua pontuação de {pont} é considerada excelente")