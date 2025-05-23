soma = 0
contador = 0

nota = float(input("Digite uma nota (-1 para terminar): "))

while nota != -1:
    soma += nota
    contador += 1
    nota = float(input("Digite outra nota (-1 para terminar): "))

if contador > 0:
    media = soma / contador
    print(f"Média das notas: {media:.2f}")
else:
    print("Nenhuma nota válida foi digitada.")
