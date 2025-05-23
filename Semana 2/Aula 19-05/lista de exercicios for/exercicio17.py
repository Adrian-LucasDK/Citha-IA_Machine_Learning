produtos = ['Caderno', 'Caneta', 'Lápis', 'Borracha', 'Estojo']
precos = [25.0, 2.5, 1.0, 3.0, 20.0]
limite = 10.0

for i in range(len(produtos)):
    if precos[i] > limite:
        print(f"Os seguintes produtos são mais caros que R$10: {produtos[i]}")
