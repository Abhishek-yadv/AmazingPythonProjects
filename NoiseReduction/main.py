# Spectral Subtraction: Method used for noise reduction
from scipy.io import wavfile
import numpy as np
import matplotlib.pyplot as plt
import os
from pydub import AudioSegment

import dataclass
print(dir(dataclass))
def read_audio(file_path):
    file_extension = os.path.splitext(file_path)[1].lower()
    if file_extension == '.wav':
        sr, data = wavfile.read(file_path)
    elif file_extension in ['.mp3', '.mp4']:
        audio = AudioSegment.from_file(file_path)
        sr = audio.frame_rate
        data = np.array(audio.get_array_of_samples())
        if audio.channels == 2:
            data = data.reshape((-1, 2))
    else:
        raise ValueError(
            "Unsupported file format. Please provide a WAV, MP3, or MP4 file.")
    return sr, data


file = input("Enter the file path: ")
sr, data = read_audio(file)

fl = 400  # frame_length
frames = []  # empty list

for i in range(0, int(len(data) / (int(fl / 2)) - 1)):
    arr = data[int(i * int(fl / 2)):int(i * int(fl / 2) + fl)]
    frames.append(arr)  # appending each array data into the frames list

frames = np.array(frames)  # converting the frames list into an array
ham_window = np.hamming(fl)  # using np.hamming
# multiplying frames array with ham_window
windowed_frames = frames * ham_window

dft = []  # empty list containing fft of windowed_frames
for i in windowed_frames:
    dft.append(np.fft.fft(i))  # taking the Fourier transform of each window

dft = np.array(dft)  # converting dft into array
dft_mag_spec = np.abs(dft)  # converting dft into absolute values
dft_phase_spec = np.angle(dft)  # finding dft angle

noise_estimate = np.mean(dft_mag_spec, axis=0)  # mean noise estimate
noise_estimate_mag = np.abs(noise_estimate)  # absolute value

estimate_mag = dft_mag_spec - 2 * noise_estimate_mag  # subtraction method
estimate_mag[estimate_mag < 0] = 0

# calculating the final estimate
estimate = estimate_mag * np.exp(1j * dft_phase_spec)

ift = []  # list containing inverse Fourier transform of estimate
for i in estimate:
    ift.append(np.fft.ifft(i))  # appending in ift list

clean_data = []
# extending clean_data containing ift list
clean_data.extend(ift[0][:int(fl / 2)])
for i in range(len(ift) - 1):
    clean_data.extend(ift[i][int(fl / 2):] + ift[i + 1][:int(fl / 2)])
# extending clean_data containing ift list
clean_data.extend(ift[-1][int(fl / 2):])

clean_data = np.array(clean_data)  # converting it into array

# Plotting the graph showing the difference in the noise
fig = plt.figure(figsize=(8, 5))
ax = plt.subplot(1, 1, 1)
ax.plot(np.linspace(0, 64000, 64000), data, label='Original', color="orange")
ax.plot(np.linspace(0, 64000, 64000), clean_data,label='Filtered', color="purple")
ax.legend(fontsize=12)
ax.set_title('Spectral Subtraction Method', fontsize=15)

filename = os.path.basename(file)
cleaned_file = "(Filtered_Audio)" + filename  # final filtered audio file name
wavfile.write(cleaned_file, rate=sr, data=clean_data.astype(np.int16))
# saved file name as audio.wav(Spectral Subtraction graph).jpg
plt.savefig(filename + "(Spectral Subtraction graph).jpg")

