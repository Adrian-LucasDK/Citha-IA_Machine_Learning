meta = 10000
vendas = [
    ['João', 15000],
    ['Julia', 27000],
    ['Marcus', 9900],
    ['Maria', 3750],
    ['Ana', 10300],
    ['Alon', 7870],
]

print("Vendedores que bateram a meta:\n")

for vendedor in vendas:
    nome = vendedor[0]
    valor = vendedor[1]
    if valor >= meta:
        print(f"{nome} vendeu R$ {valor}")
