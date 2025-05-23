def losango ():
    diagonal_Maior = float(input("Digite a Diagonal Maior do seu Losango: "))
    diagonal_Menor = float(input("Digite a Diagonal Menor do seu Losango: "))
    area = diagonal_Maior * diagonal_Menor / 2

    print(f"O triângulo com base {diagonal_Maior} e altura {diagonal_Menor} tem área de: {area:.1f}")

def triangulo ():
    base = float(input("Digite a base do seu triângulo: "))
    altura = float(input("Digite a altura do seu triângulo: "))
    area = base * altura / 2

    print(f"O triângulo com base {base} e altura {altura} tem área de: {area:.1f}")

def retangulo ():
    base = float(input("Digite a base do seu triângulo: "))
    altura = float(input("Digite a altura do seu triângulo: "))
    area = base * altura

    print(f"O retângulo com base {base} e altura {altura} tem área de: {area:.1f}")

def circulo ():
    raio = float(input("Digite o raio do seu círculo: "))
    area = 3.14 * (raio ** 2)

    print(f"O círculo com raio {raio} tem área de: {area:.1f}")

def quadrado():
    lado = float(input("Digite o lado do seu quadrado: "))
    area = lado ** 2

    print(f"O quadrado com lado {lado} tem área de: {area:.1f}")

def trapezio():
    base_Maior = float(input("Digite a base maior do seu trapézio: "))
    base_Menor = float(input("Digite a base menor do seu trapézio: "))
    altura = float(input("Digite a altura do seu trapézio: "))
    area = ((base_Maior + base_Menor) * altura) / 2

    print(f"O trapézio com bases {base_Maior} e {base_Menor} e altura {altura} tem área de: {area:.1f}")

def formas ():
    print("Escolha uma forma geométrica:")
    print("1 - Losango")
    print("2 - Triângulo")
    print("3 - Retângulo")
    print("4 - Círculo")
    print("5 - Quadrado")
    print("6 - Trapézio")
    print("7 - Sair")

    opcao = int(input("Digite o número da opção desejada: "))

    if opcao == 1:
        losango()
    elif opcao == 2:
        triangulo()
    elif opcao == 3:
        retangulo()
    elif opcao == 4:
        circulo()
    elif opcao == 5:
        quadrado()
    elif opcao == 6:
        trapezio()
    elif opcao == 7:
        print("Saindo...")
        exit()
    else:
        print("Opção inválida.")

formas()