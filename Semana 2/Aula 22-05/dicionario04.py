aluno = {'nome': 'João', 'idade': 17, 'nota': 9.5} 

print(aluno)  # {'nome': 'João', 'idade': 17, 'nota': 9.5}

del aluno['idade'] 
aluno.pop('nota') 

print(aluno)  # {'nome': 'João'}