# Standalone FFT demo — no hardware needed
# Author: Gilberto Galvis
# Use this to understand the FFT output before connecting real hardware

import numpy as np
import matplotlib.pyplot as plt
from scipy.fftpack import fft

def nextpow2(n):
    # returns the next power of 2 >= n
    # FFT runs fastest when input length is a power of 2
    m_f = np.log2(n)
    m_i = np.ceil(m_f)
    return int(2 ** m_i)

# --- Test signal ---
N = 16      # number of samples
Fs = 10     # sampling frequency in Hz
y = np.array([0, 0, 0, 0, 0, 10, 10, 10, 10, 10, 10, 0, 0, 0, 0, 0])  # square pulse

# --- FFT ---
L = len(y)
NFFT = nextpow2(L)                              # zero-pad to next power of 2
ffty = fft(y, NFFT)
xf = Fs / 2.0 * np.linspace(0, 1, NFFT // 2 + 1)  # frequency axis up to Nyquist (Fs/2)
ya = 2.0 / N * np.abs(ffty[0:NFFT // 2 + 1])       # single-sided amplitude spectrum

plt.plot(xf, ya)
plt.title('Fast Fourier Transform')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Amplitude')
plt.grid()
plt.show()
