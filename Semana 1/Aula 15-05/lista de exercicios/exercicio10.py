mes = int(input("Digite um número correspondente a semana (Janeiro = 1 e assim respectivamente): "))


match mes:
    case 1:
        print("O mês que você selecionou é Janeiro e ele tem 31 dias")
    case 2:
        print("O mês que você selecionou é Fevereiro e ele tem 28 dias")
    case 3:
        print("O mês que você selecionou é Março e ele tem 31 dias")
    case 4:
        print("O mês que você selecionou é Abril e ele tem 30 dias")
    case 5:
        print("O mês que você selecionou é Maio e ele tem 31 dias")
    case 6:
        print("O mês que você selecionou é Junho e ele tem 30 dias")
    case 7:
        print("O mês que você selecionou é Julho e ele tem 31 dias")
    case 8:
        print("O mês que você selecionou é Agosto e ele tem 31 dias")
    case 9:
        print("O mês que você selecionou é Setembro e ele tem 30 dias")
    case 10:
        print("O mês que você selecionou é Outubro e ele tem 31 dias")
    case 11:
        print("O mês que você selecionou é Novembro e ele tem 30 dias")
    case 12:
        print("O mês que você selecionou é Dezembro e ele tem 31 dias")
    case _:
        print("Número inválido. Digite um número de 1 a 12.")