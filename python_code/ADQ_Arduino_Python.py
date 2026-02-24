# Real-time data acquisition from Arduino over serial
# Author: Gilberto Galvis

import time
import serial
import numpy as np
import matplotlib.pyplot as plt
from G5libs import G5tictoc

# --- Config ---
PORT = 'COM4'       # change to your port (e.g. '/dev/ttyUSB0' on Linux)
BAUD = 115200
N = 1024            # total number of samples to display
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
# Reads one sample per 1/Fs seconds
# Sliding window: shifts buffer left and appends new sample at the end
tictoc.tic()
while i < N:
    if tictoc.toc() >= 1.0 / Fs:
        tictoc.tic()
        while ser.inWaiting() > 0:  # flush buffer, keep only latest value
            dato = ser.readline()
        y[0:-1] = y[1:]             # shift buffer left
        y[-1] = float(dato)         # append new sample
        i += 1
        graf.set_ydata(y)
        fig.canvas.draw()

ser.close()
