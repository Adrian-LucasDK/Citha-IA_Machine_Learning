agenda = {'Maria': '9922-4455', 'João': '9888-3322'}

nome = 'Maria'

if nome in agenda:
    print(f'Telefone de {nome}:', agenda[nome])
else:
    print(f'{nome} não está na agenda.')
