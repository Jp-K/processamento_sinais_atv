import numpy as np
import matplotlib.pyplot as plt

N_th = 16

th = 0

audio = np.memmap("./Anexo_38986931.pcm", dtype='h', mode='r')

#tamanho_eco = 8
#audio = np.zeros(100)
#audio[0] = 1

len_audio = len(audio)
vet_saida = np.zeros(len_audio)
vet_th = np.zeros(N_th)

for j in range(len(audio)):
    input_val = audio[j]
    y = input_val
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