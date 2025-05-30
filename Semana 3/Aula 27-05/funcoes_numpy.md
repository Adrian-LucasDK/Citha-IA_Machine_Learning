
# Funções úteis do NumPy que você talvez não conheça

## 1️⃣ flatten()

**O que faz:**  
Transforma um array multidimensional em um array unidimensional (vetor).

**Exemplo de uso:**  
```python
a = np.array([[1, 2], [3, 4]])
a.flatten()
# Saída: array([1, 2, 3, 4])
```

**Para que serve:**  
Muito útil quando você precisa "achatar" uma matriz para trabalhar com uma única dimensão.

---

## 2️⃣ where()

**O que faz:**  
Retorna os índices onde uma condição é satisfeita ou permite realizar operações condicionais.

**Exemplo de uso:**  
```python
a = np.array([1, 2, 3, 4, 5])
np.where(a > 3)
# Saída: (array([3, 4]),)

# Uso condicional
np.where(a > 3, 'maior', 'menor')
# Saída: array(['menor', 'menor', 'menor', 'maior', 'maior'], dtype='<U5')
```

**Para que serve:**  
Filtrar, localizar ou aplicar condições nos arrays de forma eficiente.

---

## 3️⃣ random.rand()

**O que faz:**  
Gera números aleatórios entre 0 e 1 com distribuição uniforme.

**Exemplo de uso:**  
```python
np.random.rand(2, 3)
``

**Para que serve:**  
Gerar dados aleatórios, muito usado em simulações, testes, inicialização de algoritmos e modelos.

---
