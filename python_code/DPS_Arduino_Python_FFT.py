import time
import serial
import numpy as np
import matplotlib.pyplot as plt
from scipy.fftpack import fft
from G5libs import G5tictoc , G5math

tictoc=G5tictoc.Timer()
fig=plt.figure()

serial=serial.Serial('COM4', 38400)#9600#38400
time.sleep(3)
serial.write("a")

N = 1024
Fs = 1000
i = 0
y = np.zeros(N)
t = np.linspace(0,((N-1)/Fs),N)

graf, = plt.plot(t, y)
plt.setp(graf, color='r', linewidth=2.0)
plt.axis([0,(N-1)/Fs,-0.1, 1024])
plt.title('Real Time DAQ')
plt.xlabel('Tiempo (t)')
plt.ylabel('Voltaje (V)')
fig.canvas.draw()
plt.show(block=False)

tictoc.tic()
while i<N:
    if tictoc.toc() >= 1.0/Fs:
        tictoc.tic()
        while serial.inWaiting() > 0:
            dato=serial.readline()
        y[0:-1] = y[1:]
        y[len(y)-1]=float(dato)
        i+=1
        graf.set_ydata(y)
        fig.canvas.draw()
        
#graf.set_ydata(y)
#fig.canvas.draw()           
#FFT
plt.figure()
L=len(y)
NFFT=G5math.nextpow2(L)
ffty=fft(y,NFFT)
xf = Fs/2.0*np.linspace(0,1,NFFT/2+1)
ya = 2.0/N*np.abs(ffty[0:NFFT//2+1])
print np.amax(ya)
#print np.argmax(ya)
print xf[np.argmax(ya)]
print np.amin(ya)
#print np.argmin(ya)
print xf[np.argmin(ya)]
plt.plot(xf,ya)
plt.title('Transformada Rapida de Fourier')
plt.xlabel('Frecuencia (Hz)')
plt.ylabel('Amplitud')
plt.grid()
plt.show()

serial.close()
