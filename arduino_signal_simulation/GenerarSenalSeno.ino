// Sine wave signal generator for serial transmission
// Author: Gilberto Galvis
// Generates a sine wave and sends 512 samples over serial per trigger
// Increments frequency by 50 Hz on each trigger for multi-frequency testing

double pi = 3.14159265359;
double f = 50;    // starting frequency in Hz
double sen;
double t = 0;

void setup() {
  Serial.begin(9600);
}

void loop() {
  while (Serial.available()) {        // wait for trigger from Python
    for (int i = 0; i <= 512; i++) {
      delay(1);                       // 1ms delay = 1kHz effective sample rate
      sen = 1023 * sin(2 * pi * f * t);
      Serial.println(sen);
      t += 0.001;
    }
    f += 50;    // increment frequency for next burst
    t = 0;      // reset time for clean sine wave
  }
}
