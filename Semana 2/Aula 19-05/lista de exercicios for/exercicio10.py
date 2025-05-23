notas = [5.0, 7.5, 8.0, 6.0, 9.0, 10.0, 4.5, 3.0]

# Calcula a média
soma = 0
for nota in notas:
    soma += nota
media = soma / len(notas)

# Exibe as notas acima da média
print("Notas acima da média:", media)
for nota in notas:
    if nota > media:
        print(nota)
