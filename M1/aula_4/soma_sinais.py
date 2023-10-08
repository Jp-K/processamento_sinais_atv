import numpy as np
import matplotlib.pyplot as plt

audio_1 = np.memmap("./sen_200hz.pcm", dtype='h', mode='r')
audio_2 = np.memmap("./sen_2khz.pcm", dtype='h', mode='r')

len_audio_1 = len(audio_1)
len_audio_2 = len(audio_2)

len_maior = len_audio_1 if len_audio_1 > len_audio_2 else len_audio_2
output_sinal = np.zeros(len_maior)
for n in range(len_maior):
    valor_1 = audio_1[n] if n < len_audio_1 else 0
    valor_2 = audio_2[n] if n < len_audio_2 else 0

    output_sinal[n] = valor_1 + valor_2

plt.plot(output_sinal)
plt.title('output')
plt.show()

fp = np.memmap("./output.pcm", dtype='h', mode='w+', shape=audio_1.shape)

for i in range(audio_1.shape[0]):
    fp[i] = output_sinal[i]