import numpy as np
import matplotlib.pyplot as plt


audio = np.memmap("./Anexo_38986931.pcm", dtype='h', mode='r')
ganho = .5

copy_audio = audio.copy()

for idx, item in enumerate(audio):
    copy_audio[idx] = item*ganho

plt.plot(audio)
plt.title('Audio original')
plt.show()

plt.plot(copy_audio)
plt.title('Audio com ganho')
plt.show()

print(audio.shape[0])
fp = np.memmap("./output.pcm", dtype='h', mode='w+', shape=audio.shape)

for i in range(audio.shape[0]):
    fp[i] = copy_audio[i]

#filtered_audio_path = 'audio_com_ganho.pcm'
#wavfile.write(filtered_audio_path, sample_rate, filtered_audio.astype(np.int16))