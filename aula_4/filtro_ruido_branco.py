import numpy as np
import matplotlib.pyplot as plt

a = 0.98
b = 1 - a

tamanho_eco = 1
audio = np.zeros(100)
audio[0] = 1

len_audio = len(audio)
vetor_eco = np.zeros(tamanho_eco)
vet_saida = np.zeros(len_audio)

for j in range(len(audio)):
    input_val = audio[j]
    y = b * input_val + a * vetor_eco[-1]
    vetor_eco[0] = y
    for k in range(tamanho_eco - 1):
        vetor_eco[tamanho_eco - k - 1] = vetor_eco[tamanho_eco - k - 2]
    vet_saida[j] = y


plt.stem(np.arange(0, 100, 1), vet_saida, linefmt='r', markerfmt='ro', basefmt='r')
plt.xlabel('x')
plt.ylabel('y')
plt.title(f'Impulso Unitário')
plt.show()


audio = np.memmap("./ruido_branco.pcm", dtype='h', mode='r')

len_audio = len(audio)
vetor_eco = np.zeros(tamanho_eco)
vet_saida = np.zeros(len_audio)

for j in range(len(audio)):
    input_val = audio[j]
    y = b * input_val + a * vetor_eco[-1]
    vetor_eco[0] = y
    for k in range(tamanho_eco - 1):
        vetor_eco[tamanho_eco - k - 1] = vetor_eco[tamanho_eco - k - 2]
    vet_saida[j] = y


plt.plot(audio)
plt.title('entrada')
plt.show()

plt.plot(vet_saida)
plt.title('output')
plt.show()

fp = np.memmap("./output_delay_ruido_branco.pcm", dtype='h', mode='w+', shape=audio.shape)

for i in range(audio.shape[0]):
    fp[i] = vet_saida[i]




audio_1 = np.memmap("./ruido_branco.pcm", dtype='h', mode='r')
audio_2 = np.memmap("./sen_80Hz.pcm", dtype='h', mode='r')

len_audio_1 = len(audio_1)
len_audio_2 = len(audio_2)

len_maior = len_audio_1 if len_audio_1 > len_audio_2 else len_audio_2
audio = np.zeros(len_maior)
for n in range(len_maior):
    valor_1 = audio_1[n] if n < len_audio_1 else 0
    valor_2 = audio_2[n] if n < len_audio_2 else 0

    audio[n] = valor_1 + valor_2

fp = np.memmap("./seno_e_ruido_branco.pcm", dtype='h', mode='w+', shape=audio.shape)

for i in range(audio.shape[0]):
    fp[i] = audio[i]

len_audio = len(audio)
vetor_eco = np.zeros(tamanho_eco)
vet_saida = np.zeros(len_audio)

for j in range(len(audio)):
    input_val = audio[j]
    y = b * input_val + a * vetor_eco[-1]
    vetor_eco[0] = y
    for k in range(tamanho_eco - 1):
        vetor_eco[tamanho_eco - k - 1] = vetor_eco[tamanho_eco - k - 2]
    vet_saida[j] = y


plt.plot(audio)
plt.title('entrada')
plt.show()

plt.plot(vet_saida)
plt.title('output')
plt.show()

fp = np.memmap("./output_delay_ruido_branco_e_seno_80Hz.pcm", dtype='h', mode='w+', shape=audio.shape)

for i in range(audio.shape[0]):
    fp[i] = vet_saida[i]