n1 = int(input("Digite o número: "))
n2 = int(input("Digite o número: "))


if n1 > n2:
    print(f"o número {n1} é maior que o número {n2}")
elif n1 < n2:
    print(f"o número {n2} é maior que o número {n1}")
elif n1 == n2:
    print(f"Os números {n1} e {n2} são iguais")
else:
    print("Ocorreu um ero")