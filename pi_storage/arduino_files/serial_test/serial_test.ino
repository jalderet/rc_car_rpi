void setup() {
  // put your setup code here, to run once:
  Serial1.begin(115200);

}

void loop() {
  // put your main code here, to run repeatedly:
  if (Serial.available() > 0)
  {
    byte x = Serial.read();
    Serial.println((char)x);
  }

}
