numero = input("Digite um número inteiro: ")

# Remover sinal negativo, se houver
if numero.startswith('-'):
    numero = numero[1:]

contador = 0
indice = 0

while indice < len(numero):
    contador += 1
    indice += 1

print(f"O número {numero} tem {contador} dígitos.")
