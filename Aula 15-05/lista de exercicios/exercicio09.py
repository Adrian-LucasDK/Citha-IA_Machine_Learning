dia = int(input("Digite um número correspondente a semana (Domingo = 1 e assim respectivamente): "))

match dia:
    case 1:
        print("O dia que você selecionou é Domingo")
    case 2:
        print("O dia que você selecionou é Segunda")
    case 3:
        print("O dia que você selecionou é Terça")
    case 4:
        print("O dia que você selecionou é Quarta")
    case 5:
        print("O dia que você selecionou é Quinta")
    case 6:
        print("O dia que você selecionou é Sexta")
    case 7:
        print("O dia que você selecionou é Sábado")
    case _:
        print("Número inválido. Digite um número de 1 a 7.")