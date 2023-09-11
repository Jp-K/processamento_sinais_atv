import numpy as np
import matplotlib.pyplot as plt

Fs = 8000
T = 200*(10**-3)
a = 0.9
b = 0.5
tamanho_eco = int(Fs*T)
audio = np.memmap("./Anexo_38986931.pcm", dtype='h', mode='r')

#tamanho_eco = 8
#audio = np.zeros(100)
#audio[0] = 1

len_audio = len(audio)
vetor_eco = np.zeros(tamanho_eco)
vet_saida = np.zeros(len_audio)

for j in range(len(audio)):
    input_val = audio[j]
    y = a * input_val + b * vetor_eco[-1]
    vetor_eco[0] = y
    for k in range(tamanho_eco - 1):
        vetor_eco[tamanho_eco - k - 1] = vetor_eco[tamanho_eco - k - 2]
    vet_saida[j] = y


#plt.stem(np.arange(0, 100, 1), vet_saida, linefmt='r', markerfmt='ro', basefmt='r')
#plt.xlabel('x')
#plt.ylabel('y')
#plt.title(f'Impulso Unitário')
#plt.show()

plt.plot(vet_saida)
plt.title('output')
plt.show()

fp = np.memmap("./output_eco.pcm", dtype='h', mode='w+', shape=audio.shape)

for i in range(audio.shape[0]):
    fp[i] = vet_saida[i]