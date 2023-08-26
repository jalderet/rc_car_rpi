#include <SparkFunMPU9250-DMP.h>
MPU9250_DMP imu;

void setup() {
  // put your setup code here, to run once:
  imu.begin();

  imu.dmpBegin(DMP_FEATURE_SEND_RAW_ACCEL, 10);

}

void loop() {
  // put your main code here, to run repeatedly:

}
