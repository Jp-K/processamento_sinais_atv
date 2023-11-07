import numpy as np
import matplotlib.pyplot as plt
from scipy import signal as sf



# EQUALIZADOR
FS = 8000
FC = 200
FC2 = 800
M = int(4/(FC2/FS))
#M = 100  # Set filter length (101 points)
print(M)
H = np.zeros(M+1)
H2 = np.zeros(M+1)
H3 = np.zeros(M+1)
OUTPUT = np.zeros(M+1)

PI = np.pi
#FC = 0.1  # Set the cutoff frequency (between 0 and 0.5) 
FC = FC/FS
FC2 = FC2/FS

# 1 = blackman | 2 = hamming
op = 2

GB = 0.7
GA = 0.6
GF = 0.5

for I in range(M+1):
    if (I - M // 2) == 0:
        H[I] = 2 * PI * FC
    if (I - M // 2) != 0:
        H[I] = np.sin(2 * PI * FC * (I - M // 2)) / (I - M // 2)
    if op == 1:
        H[I] = H[I] * (0.42 - 0.5 * np.cos(2 * PI * I / M) + 0.08 * np.cos(4 * PI * I / M))
    else:
        H[I] = H[I] * (0.54 - 0.46 * np.cos(2 * PI * I / M))

SUM = sum(H)
H = [h / SUM for h in H]

for I in range(M+1):
    if (I - M // 2) == 0:
        H2[I] = 2 * PI * FC2
    if (I - M // 2) != 0:
        H2[I] = np.sin(2 * PI * FC2 * (I - M // 2)) / (I - M // 2)
    if op == 1:
        H2[I] = H2[I] * (0.42 - 0.5 * np.cos(2 * PI * I / M) + 0.08 * np.cos(4 * PI * I / M))
    else:
        H2[I] = H2[I] * (0.54 - 0.46 * np.cos(2 * PI * I / M))

SUM = sum(H2)
H2 = [h / SUM for h in H2]

for I in range(M+1):
    H2[I] = -H2[I]
H2[int(M/2)] = H2[int(M/2)] + 1

for I in range(M+1):
    H3[I] = H[I] + H2[I]

for I in range(M+1):
    H3[I] = -H3[I]

H3[int(M/2)] = H3[int(M/2)] + 1

for I in range(M+1):
    OUTPUT[I] = H[I]*GB + H2[I]*GA + H3[I]*GF

with open("filter_kernel.dat", "w") as file:
    for value in OUTPUT:
        file.write(f"{value:.8f},\n")
plt.subplot(1,2,1)
plt.plot(OUTPUT)
plt.xlabel('Filtro equalizador')


[w, h] = sf.freqz(OUTPUT, 1,FS)

plt.subplot(1,2,2)
plt.plot(w*FS/(2*np.pi), 20*np.log10(abs(h)))
plt.xlabel('Magnitude da resposta em frequencia')

plt.show()