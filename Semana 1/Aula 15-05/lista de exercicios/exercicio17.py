sexo = input("Digite seu sexo sendo M para Masculino e F para Feminino: ")

if sexo == "M" or sexo == "m":
    print("Bem-vindo")
elif sexo == "F" or sexo == "f":
    print("Bem-vinda")
else:
    print("Operação Inválida! Use apenas M ou F")