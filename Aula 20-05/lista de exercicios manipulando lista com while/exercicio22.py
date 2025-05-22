nomes = []
contador = 0

while contador < 10:
    nome = input(f"Digite o nome {contador + 1}: ")
    nomes.append(nome)
    contador += 1

print("Nomes digitados:", nomes)
