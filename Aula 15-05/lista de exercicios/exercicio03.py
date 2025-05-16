n = int(input("Digite o número: "))

d = n % 3

if d == 0 and n != 0:
    print(f"o número {n} é divisivel por 3")
elif d != 0 and n != 0:
    print(f"o número {n} não é divisivel por 3")
else:
    print(f"o número {n} é neutro")