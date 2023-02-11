/*
    SERIAL_PORT_TESTER.INO

    BY: ALBERTO BRUNO SILVESTRE DE OLIVEIRA

    GITHUB: 
 */

int seconds = 0;
int delayMs = 1000;

void setup() {
  // Open Serial port and set speed
  Serial.begin(9600);
  }

void loop() {
  // Print to serial every second
  delay(delayMs);
  seconds += 1;
  Serial.println("Hello World!");
  Serial.print("Seconds: "); Serial.println(seconds);
}
