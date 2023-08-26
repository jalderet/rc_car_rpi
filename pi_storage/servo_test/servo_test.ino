
#include <Servo.h>

Servo esc;
int fwd = 92;


void setup() {
  // put your setup code here, to run once:

esc.attach(3);
esc.write(fwd);
delay(1000);
esc.write(130);
delay(1000);
esc.write(135);
delay(1000);
esc.write(fwd);
delay(1000);

for (int n = 50; n < 135; n++){
  esc.write(n);
  delay(10);
}
for (int j = 135; j > 50; j--){
  esc.write(j);
  delay(10);
}
esc.write(fwd);
delay(1000);

}

void loop() {
  // put your main code here, to run repeatedly:


}
