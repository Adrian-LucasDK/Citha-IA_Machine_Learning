def nome_mais_longo(nome1, nome2):
    if len(nome1) >= len(nome2):
        return nome1
    else:
        return nome2

print(nome_mais_longo("Ana", "João"))  # Saída: João