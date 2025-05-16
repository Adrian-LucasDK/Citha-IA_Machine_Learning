num1 = int(input("Digite um número: "))

if num1 > 0:
    print(f"O número {num1} é positivo")
elif num1 < 0:
    print(f"O número {num1} é negativo")
elif num1 == 0:
    print(f"O número {num1} é neutro")
else:
    print(f"Ocorreu um erro")