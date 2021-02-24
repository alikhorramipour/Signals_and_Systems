import matplotlib.pyplot as plt
import numpy as np
import wave


def triangle_filter(n):
    input = n % 80
    if input <= 40:
        return 0.000625 * input
    else:
        return (-0.000625 * (input - 40)) + 0.025

fig, axs = plt.subplots(3)

input_file = wave.open('giggle_mono.wav', mode='r')
input_bytes = input_file.readframes(input_file.getnframes())
input_data = np.frombuffer(input_bytes, dtype=np.int16)

axs[0].plot(range(5000, 8000), input_data[5000:8000])
axs[0].set_title('giggle_mono.wav')

triangle_filter_stored = []
for index in range(0, 81):
    triangle_filter_stored.append(triangle_filter(index))

axs[1].plot(range(0, len(triangle_filter_stored)), triangle_filter_stored)
axs[1].set_title('Filter')

output_data = np.convolve(input_data, triangle_filter_stored, mode='same')
# to have the same volume as the input
output_data = output_data * 2.5
output_data = np.int16(output_data)

axs[2].plot(range(5000, 8000), output_data[5000:8000])
axs[2].set_title('giggle_mono_smoothed.wav')
plt.show()

output_file = wave.open('giggle_mono_smoothed.wav', mode='wb')
output_file.setparams(input_file.getparams())
output_file.setnframes(len(output_data))
output_file.writeframes(output_data)

"""
Explaining why triangle_filter smooths out the input:
    Triangle filter includes nearby points when convolving with another signal, therefore, spikes are 'normalized'
        based on the nearby points; erratic behavior is removed and output is 'smoother'.

"""