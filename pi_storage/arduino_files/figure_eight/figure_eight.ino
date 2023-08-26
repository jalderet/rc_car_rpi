#include <Servo.h>

Servo srv;
Servo esc;
int min_speed = 101.5;
int fwd = 92;


void setup() {
  // put your setup code here, to run once:

esc.attach(3);
srv.attach(9);

srv.write(fwd);              //straight
esc.write(min_speed);
delay(3500);

srv.write(135);              //turn right
esc.write(min_speed);        
delay(6500);

srv.write(fwd);              //straight
esc.write(min_speed);
delay(3500);

srv.write(50);               //turn left
esc.write(min_speed);
delay(6500);

srv.write(fwd);              //stop
esc.write(90);
delay(1000);
}

void loop() {
  // put your main code here, to run repeatedly:


}
