import numpy as np
import matplotlib.pyplot as plt

Fs = 8000

t3 = 5 * 10 ** -3

n3 = int(t3 * Fs)
tama_media = n3

audio = np.memmap("./Anexo_38986931.pcm", dtype='h', mode='r')
copy_audio = audio.copy()
vetor_delay = np.zeros((tama_media,))

vet_saida = np.zeros_like(audio)

for j in range(len(audio)):
    input_val = copy_audio[j]
    vetor_delay[0] = input_val
    media = 0
    for item in vetor_delay:
        media += item/len(vetor_delay)
    y = media
    
    for k in range(tama_media - 1):
        vetor_delay[tama_media - k - 1] = vetor_delay[tama_media - k - 2]
    
    vet_saida[j] = y

plt.plot(audio)
plt.title('Audio original')
plt.show()

plt.plot(vet_saida)
plt.title('Audio com delay')
plt.show()

fp = np.memmap("./output_media_movel.pcm", dtype='h', mode='w+', shape=audio.shape)

for i in range(audio.shape[0]):
    fp[i] = vet_saida[i]