import numpy as np
import matplotlib.pyplot as plt

N_th = 16
P_th = 40000


audio = np.memmap("./Anexo_38986931.pcm", dtype='h', mode='r')

#tamanho_eco = 8
#audio = np.zeros(100)
#audio[0] = 1

len_audio = len(audio)
vet_saida = np.zeros(len_audio)
vet_th = np.zeros(N_th)

multiplier_N_th = 1
current_N_th = N_th
media_atual = 0
for i in range(len(audio)):
    input_val = audio[i]
    if i >= (N_th*multiplier_N_th):
        multiplier_N_th += 1
        media_atual = 0
    for j in range((N_th*(multiplier_N_th-1)),(N_th*multiplier_N_th)):
        if j <= len(audio)-1:
            valor = audio[j]
            if audio[j] < 0:
                valor = valor*-1
            media_atual += (valor)/N_th
    if media_atual >= P_th:
        vet_saida[i] = input_val
    else: 
        vet_saida[i] = 0
#plt.stem(np.arange(0, 100, 1), vet_saida, linefmt='r', markerfmt='ro', basefmt='r')
#plt.xlabel('x')
#plt.ylabel('y')
#plt.title(f'Impulso Unitário')
#plt.show()

plt.plot(audio)
plt.title('output')
plt.show()

plt.plot(vet_saida)
plt.title('output')
plt.show()

fp = np.memmap("./output_analise_potencia.pcm", dtype='h', mode='w+', shape=audio.shape)

for i in range(audio.shape[0]):
    fp[i] = vet_saida[i]