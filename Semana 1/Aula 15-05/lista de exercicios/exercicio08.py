letra = input("Digite uma letra: ")

if not letra.isalpha():
    print("Entrada inválida. Digite apenas uma letra.")
elif letra.lower() in 'aeiou':
    print(f"A letra {letra} é uma vogal.")
else:
    print(f"A letra {letra} é uma consoante.")
