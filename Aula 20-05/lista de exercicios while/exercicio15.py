numero_secreto = 7  # Defina o número secreto
tentativa = int(input("Tente adivinhar o número secreto: "))

while tentativa != numero_secreto:
    print("❌ Você errou. Tente novamente!")
    tentativa = int(input("Tente adivinhar o número secreto: "))

print("✅ Parabéns! Você acertou o número secreto!")
