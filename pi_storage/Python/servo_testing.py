#!/usr/bin/env python3
import RPi.GPIO as GPIO
from time import sleep

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(32, GPIO.OUT)
servo = GPIO.PWM(32, 200)


servo.start(30)
print('1 sec delay')
sleep(1)

def turn(duty):
    servo.ChangeDutyCycle(duty)
    
#turn(30)
#sleep(2)
#turn(25)
#sleep(2)
#turn(22)
#sleep(2)
#turn(30)
#sleep(1)

x = 30

while x < 50:
    turn(x)
    sleep(.025)
    x += .5
    
while x > 21:
    turn(x)
    sleep(.025)
    x -= .5
    
while x < 30:
    turn(x)
    sleep(.025) 
    x += .5
    
print('done with sequence')

turn(30)
sleep(1)
#print('done')
    


#servo.ChangeDutyCycle(40)
#sleep(1)

#servo.ChangeDutyCycle(80)
#sleep(1)

servo.stop(30)
#GPIO.cleanup()
print('done')




