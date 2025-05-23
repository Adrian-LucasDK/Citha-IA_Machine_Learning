#Input: base e altura
base_maior = float(input("Digite a base maior do trapézio: "))
base_menor = float(input("Digite a base menor do trapézio: "))
altura = float(input("Digite a altura do trapézio: "))

#Cálculo da área
area = ((base_maior+base_menor)*altura)/2

#Imprime a área
print(f"A área em metros quadrados é igual a {area:.1f}m²")