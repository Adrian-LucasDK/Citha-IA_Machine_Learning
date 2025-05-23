sal = float(input("Digite seu sálario em R$: "))

if sal < 1000:
    sal = sal * 1.10
    print(f"Parábens você recebeu um aumento de 10% seu sálario agora é: R${sal:.2f}")
else:
    print(f"Infelizemente seu sálario de R${sal} é maior ou igual a RS1000, você não ganhará aumento")