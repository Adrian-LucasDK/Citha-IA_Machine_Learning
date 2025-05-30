import numpy as np
import time

# Criando um vetor com 10 milhões de elementos
a = np.random.rand(10_000_000)
b = np.random.rand(10_000_000)

# Forma com for
start = time.time()
resultado = np.zeros_like(a)
for i in range(len(a)):
    resultado[i] = a[i] + b[i]
print("Tempo com for:", time.time() - start)

# Forma vetorizada
start = time.time()
resultado = a + b
print("Tempo vetorizado:", time.time() - start)