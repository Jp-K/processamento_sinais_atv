import numpy as np
import matplotlib.pyplot as plt

# Definindo o tamanho da Média
M = 400

# Alocar os vetores
x = np.zeros((M, 1))
coef = np.zeros((M, 1))

# Inicializar os vetores
for j in range(M):
    coef[j, 0] = 1 / M
    x[j, 0] = 0

# Lendo o arquivo de entrada
with open('Anexo_38986931.pcm', 'rb') as fid:
    s = np.fromfile(fid, dtype=np.int16)

itera = len(s)
# Salvar parcelas intermediárias
sav_y = np.zeros(itera)

# Executa o processamento
for j in range(itera):
    x[0, 0] = s[j]
    
    # Realizar a Soma de Produto (SOP) - Convolução
    y = 0
    for n in range(M):
        y += coef[n, 0] * x[n, 0]
    
    sav_y[j] = y
    
    # Deslocar o vetor de amostra
    for n in range(M - 1, 0, -1):
        x[n, 0] = x[n - 1, 0]


plt.subplot(2, 1, 1)
plt.plot(s)
plt.grid(True)
plt.title('Entrada e saída do Filtro')

# Plotar a saída
plt.subplot(2, 1, 2)
plt.plot(sav_y)
plt.grid(True)
plt.show()

# Salvar arquivo de saída
with open('saida_mm.pcm', 'wb') as fid2:
    sav_y.astype(np.int16).tofile(fid2)