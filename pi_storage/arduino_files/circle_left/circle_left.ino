#include <Servo.h>

Servo srv;
Servo esc;
int min_speed = 106;
int fwd = 99;

void setup() {
  // put your setup code here, to run once:
esc.attach(3);
srv.attach(9);

srv.write(54);              //turn
esc.write(min_speed);
delay(10000);

srv.write(fwd);              //straight
esc.write(90);
delay(1000);

}

void loop() {
  // put your main code here, to run repeatedly:

}
