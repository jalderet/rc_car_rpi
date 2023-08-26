
#include <SparkFunMPU9250-DMP.h>

MPU9250_DMP imu;

void setup() {

  if (imu.begin() != INV_SUCCESS)
  {
      while (1)
      {
      
      }
  }
}
  // put your setup code here, to run once:

  ////imu.begin();

  //imu.dmpBegin(DMP_FEATURE_SEND_RAW_ACCEL, 10);


  //if ( imu.fifoAvailable() > 0 ) / Check for new data in the FIFO
 // {
 //   if ( imu.dmpUpdateFifo() == INV_SUCCESS )
 // }
//}

void loop() {
  // put your main code here, to run repeatedly:

}
