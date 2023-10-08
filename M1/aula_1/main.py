import numpy as np
import matplotlib.pyplot as plt

Dt = 5e-5
t = np.arange(-5e-3, 5e-3 + Dt, Dt)

f = 1000

xa = np.cos(2 * np.pi * f * t)

plt.figure(figsize=(8, 6))

plt.plot(t * 1000, xa)
plt.xlabel('Tempo [ms]')
plt.ylabel('xa(t)')
plt.title(f'Sinal de Freq = {f} Hz')

plt.tight_layout() 
plt.show()


Fs = 8000
Ts = 1 / Fs
n = np.arange(-20, 21)
xd = np.cos(2 * np.pi * n * f / Fs)
N = len(n)


plt.stem(n, xd, linefmt='r', markerfmt='ro', basefmt='r')
plt.title('Sinal Amostrado')
plt.xlabel('Amostras')
plt.ylabel('x[n]')
plt.grid(True)
plt.show()