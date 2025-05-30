
# Funções úteis do Matplotlib (pyplot) que você talvez não conheça

## 1️⃣ subplot()

**O que faz:**  
Permite criar múltiplos gráficos (subplots) na mesma figura.

**Exemplo de uso:**  
```python
plt.subplot(1, 2, 1)  # 1 linha, 2 colunas, posição 1
plt.plot(x, y)

plt.subplot(1, 2, 2)  # posição 2
plt.bar(categorias, valores)

plt.show()
```

**Para que serve:**  
Muito útil para comparar diferentes gráficos lado a lado na mesma janela.

---

## 2️⃣ figure()

**O que faz:**  
Cria uma nova figura, onde você pode definir tamanho, DPI e outras propriedades.

**Exemplo de uso:**  
```python
plt.figure(figsize=(8, 5))
plt.plot(x, y)
plt.show()
```

**Para que serve:**  
Controla o tamanho do gráfico e permite criar várias figuras independentes no mesmo script.

---

## 3️⃣ savefig()

**O que faz:**  
Salva o gráfico como imagem (PNG, JPG, PDF, SVG, etc.).

**Exemplo de uso:**  
```python
plt.plot(x, y)
plt.savefig('grafico.png')
```

**Para que serve:**  
Muito útil para salvar gráficos gerados automaticamente, seja para relatórios, apresentações ou publicação.

---
