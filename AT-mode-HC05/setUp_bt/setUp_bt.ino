#include <SoftwareSerial.h>
 
SoftwareSerial Bluetooth(2, 3); //rx|tx -> d3|d2 AT mode


void setup() {
  Serial.begin(9600);
  Bluetooth.begin(38400);
}
 
void loop() {
  if (Bluetooth.available()) {
       Serial.write(Bluetooth.read());
//       Serial.println("masuk BT");
//       Serial.println(Bluetooth.read());
  }
  if (Serial.available()) {
      Bluetooth.write(Serial.read());
//      Serial.println("masuk");
  }
}
