#!/usr/bin/env python3
import RPi.GPIO as GPIO
from time import sleep

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(33, GPIO.OUT)
GPIO.setup(32, GPIO.OUT)
drive = GPIO.PWM(33, 500)
servo = GPIO.PWM(32, 200)

drive.start(70)
servo.start(30)
print('1 sec delay')
sleep(1)

def fwd(duty):
    drive.ChangeDutyCycle(duty)

def turn(duty):
    servo.ChangeDutyCycle(duty)
    

straight = 30
min_spd = 75

    
fwd(75.5)
turn(30)
sleep(2)

x = 30

while x < 40:
    turn(x)
    fwd(74.5)
    sleep(.1)
    x += .5
    
fwd(min_spd)
turn(39)
sleep(1.5)

while x > 30:
    turn(x)
    fwd(min_spd)
    sleep(.1)
    x -= .5


while x > 21:
    turn(x)
    fwd(min_spd)
    sleep(.1)
    x -= .5
    

fwd(min_spd)
turn(21)
sleep(1.5)


while x < 30:
    turn(x)
    fwd(74.5)
    sleep(.1)
    x += .5
    
#fwd(74)
#turn(30)
#sleep(1)

drive.stop()
servo.stop()
#GPIO.cleanup()
print('done')
