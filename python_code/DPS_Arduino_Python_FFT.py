# Real-time data acquisition + FFT analysis from Arduino
# Author: Gilberto Galvis

import time
import serial
import numpy as np
import matplotlib.pyplot as plt
from scipy.fftpack import fft
from G5libs import G5tictoc, G5math

# --- Config ---
PORT = 'COM4'       # change to your port (e.g. '/dev/ttyUSB0' on Linux)
BAUD = 38400
N = 1024            # number of samples to collect before computing FFT
Fs = 1000           # sampling frequency in Hz — must match Arduino delay

# --- Setup serial and timer ---
tictoc = G5tictoc.Timer()
fig = plt.figure()

ser = serial.Serial(PORT, BAUD)
time.sleep(3)               # wait for Arduino to reset after serial connect
ser.write("a".encode())     # send trigger to start transmission

# --- Initialize buffer and time axis ---
i = 0
y = np.zeros(N)
t = np.linspace(0, (N - 1) / Fs, N)

# --- Setup real-time plot ---
graf, = plt.plot(t, y)
plt.setp(graf, color='r', linewidth=2.0)
plt.axis([0, (N - 1) / Fs, -0.1, 1024])
plt.title('Real Time DAQ')
plt.xlabel('Time (s)')
plt.ylabel('Voltage (V)')
fig.canvas.draw()
plt.show(block=False)

# --- Acquisition loop ---
# Reads one sample per 1/Fs seconds using tictoc for timing control
# Sliding window: shifts buffer left and appends new sample at the end
tictoc.tic()
while i < N:
    if tictoc.toc() >= 1.0 / Fs:
        tictoc.tic()
        while ser.inWaiting() > 0:  # flush serial buffer, keep latest value
            dato = ser.readline()
        y[0:-1] = y[1:]             # shift buffer left by one
        y[-1] = float(dato)         # append new sample
        i += 1
        graf.set_ydata(y)
        fig.canvas.draw()

# --- FFT ---
plt.figure()
L = len(y)
NFFT = G5math.nextpow2(L)          # zero-pad to next power of 2 for efficiency
ffty = fft(y, NFFT)
xf = Fs / 2.0 * np.linspace(0, 1, NFFT // 2 + 1)  # frequency axis up to Nyquist
ya = 2.0 / N * np.abs(ffty[0:NFFT // 2 + 1])       # single-sided amplitude spectrum

print("Peak frequency:", xf[np.argmax(ya)], "Hz")
print("Peak amplitude:", np.amax(ya))

plt.plot(xf, ya)
plt.title('Fast Fourier Transform')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Amplitude')
plt.grid()
plt.show()

ser.close()
