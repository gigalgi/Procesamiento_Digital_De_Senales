
double pi=3.14159265359;
double f=50,sen;
double t=0;
// the setup routine runs once when you press reset:
void setup() {
  // initialize serial communication at 9600 bits per second:
  Serial.begin(9600);
}

// the loop routine runs over and over again forever:
void loop() {
  
 while(Serial.available()){
  for(int i=0;i<=512;i++){
    delay(1);
    sen=1023*sin(2*pi*f*t);
    Serial.println(sen);
  
    t+=0.001 ;
  }

  f+=50;
  t=0;
  // delay in between reads for stability
}

}
