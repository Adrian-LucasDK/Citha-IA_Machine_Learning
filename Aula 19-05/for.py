produtos = ['coca', 'pepsi', 'guaraná', 'fanta', 'sprite', 'tubaína', 'sukita', 'kawasaki', 'soda', 'cajuína']
producao = ['15000', '12000', '10000', '8000', '6000', '4000', '2000', '1000', '500', '300', '100']

print(f"A produção do produto {produtos[0]} é de {producao[0]}")
print(f"A produção do produto {produtos[1]} é de {producao[1]}")
print(f"A produção do produto {produtos[2]} é de {producao[2]}")
print(f"A produção do produto {produtos[3]} é de {producao[3]}")
print(f"A produção do produto {produtos[4]} é de {producao[4]}")
print(f"A produção do produto {produtos[5]} é de {producao[5]}")
print(f"A produção do produto {produtos[6]} é de {producao[6]}")
print(f"A produção do produto {produtos[7]} é de {producao[7]}")
print(f"A produção do produto {produtos[8]} é de {producao[8]}")
print(f"A produção do produto {produtos[9]} é de {producao[9]}")

print("\n")

print("Usando o for")
for i in range(len(produtos)):
    print(f"A produção do produto {produtos[i]} é de {producao[i]}")