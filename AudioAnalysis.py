import numpy as np
import matplotlib.pyplot as plt
import scipy.io.wavfile as wav
from scipy.signal import find_peaks

# 读取音频文件
sample_rate, audio_data = wav.read("test.mp3")

# 转换为单声道，如果不是的话
if len(audio_data.shape) > 1:
    audio_data = audio_data[:, 0]

# 计算音频信号的快速傅立叶变换（FFT）
fft_result = np.fft.fft(audio_data)
frequencies = np.fft.fftfreq(len(fft_result), 1 / sample_rate)
amplitude_spectrum = np.abs(fft_result)

# 找到高频峰值
peaks, _ = find_peaks(amplitude_spectrum, height=1000)  # 调整高度阈值以适应您的数据

# 绘制频谱图和高频峰值
plt.figure(figsize=(12, 6))
plt.subplot(2, 1, 1)
plt.plot(frequencies, amplitude_spectrum)
plt.title('Amplitude Spectrum')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Amplitude')

plt.subplot(2, 1, 2)
plt.plot(frequencies, amplitude_spectrum)
plt.plot(frequencies[peaks], amplitude_spectrum[peaks], 'ro')  # 高频峰值用红点标记
plt.title('High Frequency Peaks')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Amplitude')

plt.tight_layout()
plt.show()

# 检查高频峰值是否存在
if len(peaks) > 0:
    print("发现高频声音！")
else:
    print("未发现高频声音。")