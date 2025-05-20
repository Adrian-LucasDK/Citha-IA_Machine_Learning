clientes = ['Maria', 'José', 'Paula', 'Carlos']
saldos = [1200, -500, 300, -150]

for i in range(len(clientes)):
    if saldos[i] < 0:
        print(f"Esses clientes tem saldo negativo: {clientes[i]}")
