alunos = ['Fernanda', 'Pedro', 'Luana', 'André', 'Gabriela']
notas = [4.0, 6.5, 3.8, 7.2, 5.0]

for i in range(len(alunos)):
    if notas[i] < 5:
        print(f"Os seguintes alunos estão reprovados: {alunos[i]}")
