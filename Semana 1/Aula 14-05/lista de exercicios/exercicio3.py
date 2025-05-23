#Input: Dois números inteiros
n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))

#Operações
adc = n1+n2
sub = n1-n2
multi = n1*n2
div = n1*n2

#Imprime as operações
print(f"A adição é igual a: {adc}")
print(f"A subtração é igual a: {sub}")
print(f"A multiplicação é igual a: {multi}")
print(f"A divisão é igual a: {div:.2f}")