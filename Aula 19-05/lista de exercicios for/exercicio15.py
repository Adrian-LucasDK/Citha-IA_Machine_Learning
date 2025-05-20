clientes = ['Roberto', 'Júlia', 'Ricardo', 'Carla', 'Sérgio']
idades = [45, 52, 37, 60, 49]

for i in range(len(clientes)):
    if idades[i] > 50:
        print(f"Os seguintes clientes tem mais de 50 anos: {clientes[i]}")
