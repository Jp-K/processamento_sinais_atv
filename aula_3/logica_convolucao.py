import numpy as np
import matplotlib.pyplot as plt
tam = 16
x = [1, 0, 0, 0, 0, 0, 0, 0]
h = np.zeros(tam)
for i in range(len(h)):
    h[i] = 1/tam
audio = np.memmap("./sweep.pcm", dtype='h', mode='r')
copy_audio = audio.copy()

x = audio

#def flip_sequence(seq):
    #return seq[::-1]

#flipped_x = flip_sequence(x)

M = len(x)
N = len(h)
L = M + N - 1

convolved_signal = np.zeros(L)

for n in range(L):
    for k in range(N):
        if n - k >= 0 and n - k < M:
            convolved_signal[n] += x[n - k] * h[k]

print(convolved_signal)


#plt.plot(audio)
#plt.title('entrada')
#plt.show()


plt.plot(convolved_signal)
plt.title('convolucao')
plt.show()

fp = np.memmap("./output_convolucao.pcm", dtype='h', mode='w+', shape=audio.shape)

for i in range(audio.shape[0]):
    fp[i] = convolved_signal[i]