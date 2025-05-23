sal = float (input("Digite o seu salário em R$: "))
desc = float (input("Digite a porcentagem do aumento de seu salário em %: "))

sf = sal + (sal*desc/100)

print (f"O seu salário é igual a: R${sf}")