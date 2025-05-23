produtos = ['Sabão', 'Detergente', 'Shampoo', 'Condicionador', 'Escova']
precos = [3.5, 2.0, 15.0, 18.5, 8.0]

for i in range(len(produtos)):
    if precos[i] < 10:
        print(f"Os seguintes produtos custam menos de R$10: {produtos[i]}")
