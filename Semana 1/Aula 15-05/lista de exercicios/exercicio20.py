n = int(input("Digite o número: "))

d = n % 5

if d == 0 and n != 0:
    print(f"o número {n} é múltiplo de 5")
elif d != 0 and n != 0:
    print(f"o número {n} não é múltiplo de 5")
else:
    print(f"o número {n} é neutro")