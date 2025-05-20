produtos = ['coca', 'pepsi', 'guaraná', 'fanta', 'sprite', 'tubaína', 'sukita', 'kawasaki', 'soda', 'cajuína']
producao = [15000, 12000, 10000, 8000, 6000, 4000, 2000, 1000, 500, 300]

for i in range(len(produtos)):
    if producao[i] > 1000:
        print(f"A produção do produto {produtos[i]} é de {producao[i]}")