import numpy as np
import matplotlib.pyplot as plt
from scipy import signal as sf
# BAND-PASS WINDOWED-SINC FILTER

M = 800
A = np.zeros(M+1)  
B = np.zeros(M+1)  
H = np.zeros(M+1)  
FS = 8000
PI = np.pi

# 1 = blackman | 2 = hamming
op = 1

FC = 0.196 
for I in range(M+1):
    if (I - M // 2) == 0:
        A[I] = 2 * PI * FC
    if (I - M // 2) != 0:
        A[I] = np.sin(2 * PI * FC * (I - M // 2)) / (I - M // 2)
    if op == 1:
        A[I] = A[I] * (0.42 - 0.5 * np.cos(2 * PI * I / M) + 0.08 * np.cos(4 * PI * I / M))
    else:
        A[I] = A[I] * (0.54 - 0.46 * np.cos(2 * PI * I / M))

SUM = sum(A)
A = [a / SUM for a in A]


FC = 0.204  
for I in range(M+1):
    if (I - M // 2) == 0:
        B[I] = 2 * PI * FC
    if (I - M // 2) != 0:
        B[I] = np.sin(2 * PI * FC * (I - M // 2)) / (I - M // 2)
    if op == 1:
        B[I] = B[I] * (0.42 - 0.5 * np.cos(2 * PI * I / M) + 0.08 * np.cos(4 * PI * I / M))
    else:
        B[I] = B[I] * (0.54 - 0.46 * np.cos(2 * PI * I / M))

SUM = sum(B)
B = [b / SUM for b in B]

for I in range(M+1):
    B[I] = -B[I]
B[int(M/2)] = B[int(M/2)] + 1

for I in range(M+1):
    H[I] = A[I] + B[I]

for I in range(M+1):
    H[I] = -H[I]

H[int(M/2)] = H[int(M/2)] + 1


with open("filter_kernel.dat", "w") as file:
    for value in H:
        file.write(f"{value:.8f},\n")


plt.subplot(1,2,1)
plt.plot(H)
plt.xlabel('Filtro passa-faixa')


[w, h] = sf.freqz(H, 1,FS)
plt.subplot(1,2,2)
plt.plot(w*FS/(2*np.pi), 20*np.log10(abs(h)))
plt.xlabel('Magnitude da resposta em frequencia')

plt.show()