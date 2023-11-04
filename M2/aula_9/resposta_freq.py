import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

numerator = [1, 0.9] 
denominator = [1, 1, 0.41]  

frequencies = np.logspace(-1, 2, 1000)

w, h = signal.freqz(numerator, denominator, worN=frequencies)

# Plote o módulo da resposta em frequência (ganho)
plt.figure()
plt.semilogx(w, abs(h))
plt.title('Resposta em Frequência')
plt.xlabel('Frequência [rad/s]')
plt.ylabel('Ganho')
plt.grid()

plt.show()