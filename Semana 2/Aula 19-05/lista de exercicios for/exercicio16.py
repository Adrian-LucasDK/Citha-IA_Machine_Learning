produtos = ['Arroz', 'Feijão', 'Macarrão', 'Óleo', 'Açúcar']
estoque = [50, 200, 30, 10, 90]
nivel_critico = 40

for i in range(len(produtos)):
    if estoque[i] < nivel_critico:
        print(f"Os seguintes estão em nivel critico de estoque: {produtos[i]}")
