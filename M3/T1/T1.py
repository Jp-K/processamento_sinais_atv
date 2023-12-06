import numpy as np
import matplotlib.pyplot as plt

TAM_COEFS = 4
passo = 1*(10**-11)
audio = np.memmap("./branco_ruido.pcm", dtype='h', mode='r')
W = np.zeros(TAM_COEFS)
samples = np.zeros(TAM_COEFS)
TAM_MEDIA = 4
P = [1/4,1/4,1/4,1/4]

len_audio = len(audio)
erro = np.zeros(len_audio)
for j in range(len(audio)):
    d = 0
    samples[0] = audio[j]
    for n in range(TAM_MEDIA):
        d += P[n]*samples[n]

    # logica conv adap
    y = 0
    for n in range(TAM_COEFS):
        y += W[n]*samples[n]
    # logica conv adap
    erro[j] = d-y

    for n in range(TAM_COEFS):
        W[n] = W[n] + passo*erro[j]*samples[n]
    

    for n in reversed(range(TAM_COEFS)):
        samples[n] = samples[n-1]
print(W)
plt.plot(erro)
plt.title('erro')
plt.show()
