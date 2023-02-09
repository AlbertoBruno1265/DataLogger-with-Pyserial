/*
    SERIAL_PORT_TESTER.INO

    BY: ALBERTO BRUNO SILVESTRE DE OLIVEIRA

    GITHUB: 
 */

 int seconds = 0;

void setup() {
  Serial.begin(9600);
  }

void loop() {
  delay(1000);
  seconds += 1;
  Serial.println("Teste");
  Serial.print("Seconds: "); Serial.println(seconds);
}
