#!/usr/bin/env python3
import RPi.GPIO as GPIO
from time import sleep

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(37, GPIO.OUT)
drive = GPIO.PWM(37, 500)


drive.start(0)
print('1 sec delay')
sleep(1)

def turn(duty):
    drive.ChangeDutyCycle(duty)
    
#turn(30)
#sleep(2)
print('last one')    
#turn(3)
#sleep(1)
#turn(22)
#sleep(2)
#turn(30)
#sleep(1)

x = 70

while x < 83:
    turn(x)
    sleep(.5)
    print(x)
    x += 1
    
#while x > 21:
 #   turn(x)
  #  sleep(.025)
   # x -= .5
    
#while x < 30:
#    turn(x)
#    sleep(.025) 
 #   x += .5
    
print('done with sequence')

turn(0)
sleep(1)
#print('done')
    


#servo.ChangeDutyCycle(40)
#sleep(1)

#servo.ChangeDutyCycle(80)
#sleep(1)

drive.stop(30)
#GPIO.cleanup()
print('done')
