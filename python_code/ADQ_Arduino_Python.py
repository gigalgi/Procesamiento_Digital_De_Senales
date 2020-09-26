import time
import serial
import numpy as np
import matplotlib.pyplot as plt
from scipy.fftpack import fft
from G5libs import G5tictoc , G5math

tictoc=G5tictoc.Timer()
fig=plt.figure()

serial=serial.Serial('COM4', 115200)#9600
time.sleep(3)
serial.write("a")

N = 1024
Fs = 1000
i=0
y=np.zeros(N)
t=np.linspace(0,((N-1)/Fs),N)


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

serial.close()
