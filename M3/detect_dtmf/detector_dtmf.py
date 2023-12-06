import numpy as np
import matplotlib.pyplot as plt

FC = 1477
FB = 40
FS = 8000

c = (np.tan((np.pi*FB)/FS)-1)/(np.tan((2*np.pi*FB)/FS)+1)
d = 0-np.cos((2*np.pi*FC)/FS)

b0 = 0-c
b1 = d*(1-c)
b2 = 1
a1 = d*(1-c)
a2 = 0-c


# tem q multiplicar os coefs por 32767 para dar cast para short lá no DSP
print(b0)
print(b1)
print(b2)
print(a1)
print(a2)
print("-----------------")
print(int((b0*32767)/2))
print(int((b1*32767)/2))
print(int((b2*32767)/2))
print(int((a1*32767)/2))
print(int((a2*32767)/2))

audio = np.memmap("./sweep.pcm", dtype='h', mode='r')


len_audio = len(audio)
vet_saida = np.zeros(len_audio)
xnm1 = 0
xnm2 = 0
ynm1 = 0
ynm2 = 0

for i in range(len(audio)):
    x = audio[i]
    y =  (b0 * x) + (b1 * xnm1) + (b2 * xnm2) - (a1 * ynm1) - (a2 * ynm2)
    xnm2 = xnm1
    xnm1 = x
    ynm2 = ynm1
    ynm1 = y
    vet_saida[i] = 0.5*(x-y)


plt.plot(vet_saida)
plt.title('output')
plt.show()

fp = np.memmap("./output_sweep.pcm", dtype='h', mode='w+', shape=audio.shape)

for i in range(audio.shape[0]):
    fp[i] = vet_saida[i]