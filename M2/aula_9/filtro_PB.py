import numpy as np
import matplotlib.pyplot as plt
from scipy import signal as sf

# LOW-PASS WINDOWED-SINC FILTER
FS = 8000
FC = 800
#M = 100  # Set filter length (101 points)
M = int(4/(FC/FS))
print(M)
H = np.zeros(M+1)
PI = np.pi
#FC = 0.14  # Set the cutoff frequency (between 0 and 0.5) 
FC = FC/FS

# 1 = blackman | 2 = hamming
op = 2


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
with open("filter_kernel.dat", "w") as file:
    for value in H:
        file.write(f"{value:.8f},\n")


plt.subplot(1,2,1)
plt.plot(H)
plt.xlabel('Filtro passa-baixa')


[w, h] = sf.freqz(H, 1,FS)
plt.subplot(1,2,2)
plt.plot(w*FS/(2*np.pi), 20*np.log10(abs(h)))
plt.xlabel('Magnitude da resposta em frequencia')

plt.show()