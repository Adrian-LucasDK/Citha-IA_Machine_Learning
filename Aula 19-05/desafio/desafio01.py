# Pergunta quantas pessoas ficarão no quarto
qtd = int(input("Quantas pessoas ficarão no quarto? (1 a 4): "))

# Lista para guardar os dados das pessoas
quarto = []

# Coleta nome e CPF de cada pessoa
for i in range(qtd):
    nome = input("Nome da pessoa: ")
    cpf = input("CPF da pessoa: ")
    quarto.append((nome, cpf))

# Mostra os dados registrados
print("\nPessoas no quarto:")
for pessoa in quarto:
    print("Nome:", pessoa[0], "- CPF:", pessoa[1])
