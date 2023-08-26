#include <Servo.h>
Servo esc;
Servo srv;
int fwd =92;
int min_speed = 100;

void setup() {
  // put your setup code here, to run once:
esc.attach(9);
srv.attach(3);

srv.write(fwd);
esc.write(160);
delay(2000);

srv.write(fwd);
esc.write(160);
delay(2000);


}

void loop() {
  // put your main code here, to run repeatedly:

}
