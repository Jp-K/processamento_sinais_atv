import numpy as np
import matplotlib.pyplot as plt

Fs = 8000

def impulso_unitario(n):
    return float(1) if float(n) == float(0.0) else 0.0

values = []
for n in np.arange(-10, 25, 0.5):
    values.append(impulso_unitario(n))

D = 1
Ts = 125.0 * 10 ** -6

n_eco = int(D * 10)
a0 = 1
a1 = 0.5
tama_eco = n_eco
vetor_eco = np.zeros((tama_eco,))
vet_saida = np.zeros_like(values)

for j in range(len(values)):
    input_val = values[j]
    vetor_eco[0] = input_val
    y = a0 * vetor_eco[0] + a1 * vetor_eco[-1]
    vetor_eco[0] = y
    for k in range(tama_eco - 1):
        vetor_eco[tama_eco - k - 1] = vetor_eco[tama_eco - k - 2]
    
    vet_saida[j] = y
plt.stem(np.arange(-10, 25, 0.5), vet_saida, linefmt='r', markerfmt='ro', basefmt='r')
plt.xlabel('x')
plt.ylabel('y')
plt.title(f'Impulso Unitário')
plt.show()
D = 100 * 10 ** -3
Ts = 125.0 * 10 ** -6

a0 = 1.0
a1 = 0.5

audio = np.memmap("./Anexo_38986931.pcm", dtype='h', mode='r')

copy_audio = audio.copy()
n_eco = int(D * Fs)
a0 = 1
a1 = 0.5
tama_eco = n_eco
vetor_eco = np.zeros((tama_eco,))

vet_saida = np.zeros_like(audio)

for j in range(len(audio)):
    input_val = copy_audio[j]
    vetor_eco[0] = input_val
    y = a0 * vetor_eco[0] + a1 * vetor_eco[-1]
    vetor_eco[0] = y
    for k in range(tama_eco - 1):
        vetor_eco[tama_eco - k - 1] = vetor_eco[tama_eco - k - 2]
    
    vet_saida[j] = y


plt.plot(audio)
plt.title('Audio original')
plt.show()

plt.plot(vet_saida)
plt.title('Audio com eco')
plt.show()

fp = np.memmap("./output_eco.pcm", dtype='h', mode='w+', shape=audio.shape)

for i in range(audio.shape[0]):
    fp[i] = vet_saida[i]