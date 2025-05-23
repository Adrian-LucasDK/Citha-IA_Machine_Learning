funcionarios = ['João', 'Mariana', 'Carlos', 'Beatriz', 'Lucas']
salarios = [2800, 3500, 2700, 4200, 3100]

for i in range(len(funcionarios)):
    if salarios[i] > 3000:
        print(f"Os seguintes funcionários recebem mais que R$3000{funcionarios[i]}")
