from scipy.io import wavfile
import numpy as np
import matplotlib.pyplot as plt
import os
from pydub import AudioSegment


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
frames = []
for i in range(0, int(len(data) / (int(fl / 2)) - 1)):
    arr = data[int(i * int(fl / 2)):int(i * int(fl / 2) + fl)]
    frames.append(arr)

frames = np.array(frames)
ham_window = np.hamming(fl)
windowed_frames = frames * ham_window

dft = np.fft.fft(windowed_frames, axis=1)
dft_mag_spec = np.abs(dft)
dft_phase_spec = np.angle(dft)

noise_estimate = np.mean(dft_mag_spec, axis=0)
noise_estimate_mag = np.abs(noise_estimate)

estimate_mag = dft_mag_spec - 2 * noise_estimate_mag
estimate_mag[estimate_mag < 0] = 0

estimate = estimate_mag * np.exp(1j * dft_phase_spec)

ift = np.fft.ifft(estimate, axis=1)
clean_data = np.zeros_like(frames, dtype=np.float64)
clean_data[:, :int(fl / 2)] += ift.real[:, :int(fl / 2)]
for i in range(len(ift) - 1):
    clean_data[:, int(fl / 2):] += ift.real[:, int(fl / 2):]
clean_data = clean_data.flatten().astype(np.int16)

fig = plt.figure(figsize=(8, 5))
ax = plt.subplot(1, 1, 1)
ax.plot(np.linspace(0, len(data), len(data)),
        data, label='Original', color="orange")
ax.plot(np.linspace(0, len(clean_data), len(clean_data)),
        clean_data, label='Filtered', color="purple")
ax.legend(fontsize=12)
ax.set_title('Spectral Subtraction Method', fontsize=15)

filename = os.path.basename(file)
cleaned_file = "(Filtered_Audio)" + filename
wavfile.write(cleaned_file, rate=sr, data=clean_data)
plt.savefig(filename + "(Spectral Subtraction graph).jpg")
plt.show()
