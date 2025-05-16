idade = int(input("Digite sua idade: "))

if idade < 0:
     print("Idade inválida, ela deve ser positiva")
elif idade >= 18:
    print(f"Você tem {idade} anos e é maior de idade")
elif idade < 18:
     print(f"Você tem {idade} anos e é menor de idade")
else:
     print("ocorreu um erro")