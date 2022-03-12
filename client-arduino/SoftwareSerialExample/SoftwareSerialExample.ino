#include <SoftwareSerial.h>

SoftwareSerial mySerial(10, 11); // RX, TX

void setup() {
  Serial.begin(57600);

   mySerial.begin(4800);
  mySerial.println("Hello, world?");
}

void loop() { // run over and over
  Serial.println(mySerial.available());
  if (mySerial.available()) {
    Serial.write(mySerial.read());
  }
  if (Serial.available()) {
    mySerial.write(Serial.read());
  }
}
