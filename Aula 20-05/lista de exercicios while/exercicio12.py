saldo = 1000  # Saldo inicial

while True:
    print("\n========= CAIXA ELETRÔNICO =========")
    print("1 - Consultar saldo")
    print("2 - Sacar")
    print("3 - Depositar")
    print("0 - Sair")
    print("=====================================")

    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        print(f"\n💰 Seu saldo atual é: R$ {saldo:.2f}")

    elif opcao == 2:
        saque = float(input("Digite o valor para saque: "))
        if saque > 0:
            if saque <= saldo:
                saldo -= saque
                print(f"✅ Saque de R$ {saque:.2f} realizado com sucesso.")
                print(f"💰 Saldo atual: R$ {saldo:.2f}")
            else:
                print("❌ Saldo insuficiente.")
        else:
            print("❌ Valor inválido para saque.")

    elif opcao == 3:
        deposito = float(input("Digite o valor para depósito: "))
        if deposito > 0:
            saldo += deposito
            print(f"✅ Depósito de R$ {deposito:.2f} realizado com sucesso.")
            print(f"💰 Saldo atual: R$ {saldo:.2f}")
        else:
            print("❌ Valor inválido para depósito.")

    elif opcao == 0:
        print("\n🚪 Saindo... Obrigado por usar nosso caixa eletrônico!")
        break

    else:
        print("❌ Opção inválida. Tente novamente.")
