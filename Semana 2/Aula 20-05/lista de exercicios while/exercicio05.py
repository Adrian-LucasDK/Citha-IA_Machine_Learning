senha_correta = "1234"
senha = input("Digite a senha: ")

while senha != senha_correta:
    print("Senha incorreta. Tente novamente.")
    senha = input("Digite a senha: ")

print("Senha correta! Acesso liberado.")
