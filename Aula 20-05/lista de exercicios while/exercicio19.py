nomes = []

while True:
    nome = input("Digite um nome (ou 'fim' para encerrar): ")
    if nome.lower() == 'fim':
        break
    nomes.append(nome)

print("Nomes digitados:")
for n in nomes:
    print(n)
