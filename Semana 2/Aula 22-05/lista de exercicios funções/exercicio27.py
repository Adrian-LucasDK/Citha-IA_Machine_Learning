def contar_vogais(texto):
    contador = 0
    for letra in texto:
        if letra in 'aeiouAEIOU':
            contador += 1
    return contador

print(contar_vogais("Aula de Python")) 