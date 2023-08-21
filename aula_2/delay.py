import numpy as np
import matplotlib.pyplot as plt

Fs = 8000
t1 = 1.0 * 10 ** -3
t2 = 1.5 * 10 ** -3

n1 = int(t1 * Fs)
n2 = int(t2 * Fs)

a0 = 0.5
a1 = 0.3
a2 = 0.2

tama_delay = n2
vetor_delay = np.zeros((tama_delay, 1))

entrada = np.zeros((2 * tama_delay, 1))
entrada[0, 0] = 1

tama_loop = len(entrada)
vet_saida = np.zeros((tama_loop, 1))

for j in range(tama_loop):
    input_val = entrada[j, 0]
    vetor_delay[0, 0] = input_val
    y = a0 * vetor_delay[0, 0] + a1 * vetor_delay[n1 - 1, 0] + a2 * vetor_delay[n2 - 1, 0]
    
    for k in range(tama_delay - 1):
        vetor_delay[tama_delay - k - 1, 0] = vetor_delay[tama_delay - k - 2, 0]
    
    vet_saida[j, 0] = y

plt.stem(vet_saida)
plt.title('Teste Delay')
plt.show()

t3 = 100 * 10 ** -3

n3 = int(t3 * Fs)

audio = np.memmap("./Anexo_38986931.pcm", dtype='h', mode='r')

copy_audio = audio.copy()

tama_delay = n3
vetor_delay = np.zeros((tama_delay,))

vet_saida = np.zeros_like(audio)

for j in range(len(audio)):
    input_val = copy_audio[j]
    vetor_delay[0] = input_val
    y = 1 * vetor_delay[0] + 0.5 * vetor_delay[n3 - 1]
    
    for k in range(tama_delay - 1):
        vetor_delay[tama_delay - k - 1] = vetor_delay[tama_delay - k - 2]
    
    vet_saida[j] = y

plt.plot(audio)
plt.title('Audio original')
plt.show()

plt.plot(vet_saida)
plt.title('Audio com delay')
plt.show()

fp = np.memmap("./output.pcm", dtype='h', mode='w+', shape=audio.shape)

for i in range(audio.shape[0]):
    fp[i] = vet_saida[i]