n = int(input("Digite o número: "))

d = n % 2

if d == 0 and n != 0:
    print(f"o número {n} é par")
elif d != 0 and n != 0:
    print(f"o número {n} é impar")
else:
    print(f"o número {n} é neutro")