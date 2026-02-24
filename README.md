[English](#english) | [Español](#español)

---

## English

# Digital Signal Processing — Arduino + Python

Real-time data acquisition from Arduino over serial and frequency analysis
using the Fast Fourier Transform (FFT). Built as a practical signal processing
toolkit for embedded sensor systems.

### What this does

Captures live sensor data from Arduino, plots it in real time, then computes
the FFT to identify dominant frequencies. Useful for analyzing vibration,
audio, motor noise, or any periodic signal from a physical sensor.

### Project structure

```
arduino_signal_simulation/
    GenerarSenalSeno.ino     — sine wave generator for testing
python_code/
    ADQ_Arduino_Python.py    — real-time acquisition and plotting
    DPS_Arduino_Python_FFT.py — acquisition + FFT analysis
    FFT.py                   — standalone FFT demo
    G5libs/
        G5math.py            — nextpow2 utility
        G5tictoc.py          — MATLAB-style tic/toc timer
```

### Usage

**1. Install dependencies**
```bash
pip install -r requirements.txt
```

**2. Upload Arduino sketch**
Upload `GenerarSenalSeno.ino` to your Arduino board.

**3. Set your serial port**
In `ADQ_Arduino_Python.py` or `DPS_Arduino_Python_FFT.py`, set:
```python
PORT = 'COM4'        # Windows
PORT = '/dev/ttyUSB0'  # Linux
PORT = '/dev/cu.usbmodem...'  # macOS
```

**4. Run**
```bash
# acquisition only
python ADQ_Arduino_Python.py

# acquisition + FFT
python DPS_Arduino_Python_FFT.py

# standalone FFT demo (no hardware needed)
python FFT.py
```

### Implementation notes

**Sliding window buffer** — the acquisition loop uses `y[0:-1] = y[1:]` to
shift the buffer and append new samples, enabling continuous real-time plotting
without storing the full history.

**nextpow2 for FFT** — FFT is most efficient when the input length is a power
of 2. `G5math.nextpow2()` finds the next power of 2 above the signal length
for zero-padded FFT computation.

**G5tictoc** — a MATLAB-style tic/toc timer that controls the acquisition
sampling rate from the Python side.

### Requirements
- Python 3.x
- Arduino board (Uno, Nano, Mega or compatible)

### License
MIT

---

## Español

# Procesamiento Digital de Señales — Arduino + Python

Adquisición de datos en tiempo real desde Arduino por puerto serial y análisis
de frecuencias mediante la Transformada Rápida de Fourier (FFT). Desarrollado
como herramienta práctica de procesamiento de señales para sistemas de sensores
embebidos.

### Qué hace

Captura datos en vivo desde Arduino, los grafica en tiempo real y calcula la
FFT para identificar frecuencias dominantes. Útil para analizar vibración,
audio, ruido de motores o cualquier señal periódica de un sensor físico.

### Estructura del proyecto

```
arduino_signal_simulation/
    GenerarSenalSeno.ino     — generador de señal senoidal para pruebas
python_code/
    ADQ_Arduino_Python.py    — adquisición y graficación en tiempo real
    DPS_Arduino_Python_FFT.py — adquisición + análisis FFT
    FFT.py                   — demo FFT sin hardware
    G5libs/
        G5math.py            — función nextpow2
        G5tictoc.py          — temporizador estilo tic/toc de MATLAB
```

### Uso

**1. Instalar dependencias**
```bash
pip install -r requirements.txt
```

**2. Cargar sketch en Arduino**
Sube `GenerarSenalSeno.ino` a tu placa Arduino.

**3. Configurar puerto serial**
En `ADQ_Arduino_Python.py` o `DPS_Arduino_Python_FFT.py`, define:
```python
PORT = 'COM4'          # Windows
PORT = '/dev/ttyUSB0'  # Linux
PORT = '/dev/cu.usbmodem...'  # macOS
```

**4. Ejecutar**
```bash
# solo adquisición
python ADQ_Arduino_Python.py

# adquisición + FFT
python DPS_Arduino_Python_FFT.py

# demo FFT sin hardware
python FFT.py
```

### Notas de implementación

**Buffer deslizante** — el loop de adquisición usa `y[0:-1] = y[1:]` para
desplazar el buffer y agregar nuevas muestras, permitiendo graficación
continua en tiempo real sin almacenar todo el historial.

**nextpow2 para FFT** — la FFT es más eficiente cuando la longitud de entrada
es potencia de 2. `G5math.nextpow2()` encuentra la siguiente potencia de 2
por encima de la longitud de la señal para el cálculo con zero-padding.

**G5tictoc** — temporizador estilo tic/toc de MATLAB que controla la tasa de
muestreo de adquisición desde el lado de Python.

### Requisitos
- Python 3.x
- Placa Arduino (Uno, Nano, Mega o compatible)

### Licencia
MIT
