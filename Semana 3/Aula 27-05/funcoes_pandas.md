
# Funções úteis do Pandas que você talvez não conheça

## 1️⃣ apply()

**O que faz:**  
Aplica uma função a cada elemento, linha ou coluna do DataFrame.

**Exemplo de uso:**  
```python
df['nova_coluna'] = df['coluna'].apply(lambda x: x * 2)
```

**Para que serve:**  
Permite transformar ou processar dados de forma flexível, usando funções próprias ou funções anônimas (`lambda`).

---

## 2️⃣ value_counts()

**O que faz:**  
Conta a frequência dos valores únicos em uma coluna.

**Exemplo de uso:**  
```python
df['categoria'].value_counts()
```

**Para que serve:**  
É muito usado na análise exploratória para entender a distribuição dos dados em uma coluna categórica.

---

## 3️⃣ astype()

**O que faz:**  
Altera o tipo de dados de uma coluna.

**Exemplo de uso:**  
```python
df['id'] = df['id'].astype(str)
```

**Para que serve:**  
Corrige tipos de dados, como transformar inteiros em strings ou floats em inteiros, muito útil quando se lê dados de arquivos externos que podem ter tipos incorretos.

---
