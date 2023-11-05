import numpy as np
import matplotlib.pyplot as plt
from scipy import signal as sf

# HIGH-PASS WINDOWED-SINC FILTER
M = 800  # Set filter length (101 points)
H = np.zeros(M+1)
FS = 8000

PI = np.pi
FC = 0.1  # Set the cutoff frequency (between 0 and 0.5) 


for I in range(M+1):
    if (I - M // 2) == 0:
        H[I] = 2 * PI * FC
    if (I - M // 2) != 0:
        H[I] = np.sin(2 * PI * FC * (I - M // 2)) / (I - M // 2)
    H[I] = H[I] * (0.54 - 0.46 * np.cos(2 * PI * I / M))

SUM = sum(H)
H = [h / SUM for h in H]

for I in range(M+1):
    H[I] = -H[I]

H[int(M/2)] = H[int(M/2)] + 1

with open("filter_kernel.dat", "w") as file:
    for value in H:
        file.write(f"{value:.8f},\n")


plt.subplot(1,2,1)
plt.plot(H)
plt.xlabel('Filtro passa-alta')


[w, h] = sf.freqz(H, 1,FS)
plt.subplot(1,2,2)
plt.plot(w*FS/(2*np.pi), 20*np.log10(abs(h)))
plt.xlabel('Magnitude da resposta em frequencia')

plt.show()