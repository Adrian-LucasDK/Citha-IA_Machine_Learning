n1 = int(input("Digite o número: "))
n2 = int(input("Digite o número: "))
n3 = int(input("Digite o número: "))


if n1 > n2 and n1 > n3:
    print(f"o número {n1} é maior que o número {n2} e {n3}")
elif n2 > n1 and n2 > n3:
    print(f"o número {n2} é maior que o número {n1} e {n3}")
elif n3 > n1 and n3 > n2:
    print(f"o número {n3} é maior que o número {n1} e {n2}")
elif n1 == n2 and n2 == n3 and n1 == n3:
    print(f"Os números {n1},{n2} e {n3} são iguais")
else:
    print("Ocorreu um ero")