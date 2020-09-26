import numpy as np
import matplotlib.pyplot as plt
from scipy.fftpack import fft
def nextpow2(n):
    m_f = np.log2(n)
    m_i = np.ceil(m_f)
    return 2**m_i

N = 16
Fs = 10
y=np.array([0,0,0,0,0,10,10,10,10,10,10,0,0,0,0,0])

#fft
L=len(y)
NFFT=int(nextpow2(L))
ffty=fft(y,NFFT)
xf = Fs/2.0*np.linspace(0,1,NFFT/2+1)
ya = 2.0/N*np.abs(ffty[0:NFFT//2+1])
plt.plot(xf,ya)
plt.title('Transformada Rapida de Fourier')
plt.xlabel('Frecuencia (Hz)')
plt.ylabel('Amplitud')
plt.grid()
plt.show()

