carrinho = ['Notebook', 'Teclado', 'Mouse'] 

precos = [2500, 100, 150]

for produto, preco in zip(carrinho, precos):
    print(f"O produto {produto} tem o valor de R${preco}")
