soma = 0
contador = 0

nota = float(input("Digite a nota do aluno (-1 para encerrar): "))

while nota != -1:
    soma += nota
    contador += 1
    nota = float(input("Digite a nota do aluno (-1 para encerrar): "))

if contador > 0:
    media = soma / contador
    print(f"A média da turma é: {media:.2f}")
else:
    print("Nenhuma nota válida foi digitada.")
