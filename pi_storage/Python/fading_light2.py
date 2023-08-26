#!/usr/bin/env python3
import RPi.GPIO as GPIO
from time import sleep

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(37, GPIO.OUT)
myPWM = GPIO.PWM(37, 100)
myPWM.start(0)

x = 0
while x < 100:
    myPWM.ChangeDutyCycle(x)
    sleep(.05)
    x += 1
    
while x > 0:
    myPWM.ChangeDutyCycle(x)
    sleep(.05)
    x -= 1
    
    

#myPWM.start(100)
#sleep(1)
#myPWM.ChangeDutyCycle(25)
#sleep(1)
#GPIO.output(37,False)

myPWM.stop(100)


