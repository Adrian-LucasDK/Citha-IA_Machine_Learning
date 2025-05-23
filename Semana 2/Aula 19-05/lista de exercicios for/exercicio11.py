alunos = ['Ana', 'Bruno', 'Carlos', 'Diana', 'Eduardo']
notas = [6.5, 8.0, 7.2, 5.5, 9.1]

for i in range(len(alunos)):
    if notas[i] > 7.0:
        print(f"Os seguintes alunos tiraram notas acima de 7: {alunos[i]}")
