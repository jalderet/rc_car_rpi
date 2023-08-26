#!/usr/bin/env python3
import RPi.GPIO as GPIO
from time import sleep

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(37, GPIO.OUT)
GPIO.setup(32, GPIO.OUT)
drive = GPIO.PWM(37, 500)
servo = GPIO.PWM(32, 200)

drive.start(70)
servo.start(30)
print('1 sec delay')
sleep(1)

def fwd(duty):
    drive.ChangeDutyCycle(duty)

def turn(duty):
    servo.ChangeDutyCycle(duty)
    
    
def straight(pwr, time):
    fwd(pwr)
    sleep(time)
    
    
def accel(pwr, time):
    x = 70
    
    while x < pwr:
        fwd(pwr)
        sleep(time)
        print(x)
        x += 1.25
        #turn(30)
    
def right_wheels(amount):
    x = 30

    while x < amount:
        turn(x)
        sleep(.1)
        x += .5
        
def left_wheels(amount):
    x = 30
    while x > amount:
        turn(x)
        sleep(.1)
        x -= .5
        
def turn_right(pwr, amount, time, starting):
    x = starting
    while x < amount:
        turn(x)
        fwd(pwr)
        sleep(time)
        x += .5
    
def turn_left(pwr, amount, time, starting):
    x = starting
    while x > amount:
        turn(x)
        fwd(pwr)
        sleep(time)
        x -= .5
        
def turn_straight_right(starting):
    x = starting
    while x > 28:
        turn(x)
        sleep(.1)
        x -= .5

def turn_straight_left(starting):
    x = starting
    while x < 30:
        turn(x)
        sleep(.1)
        x += .5
        
turn_straight_left(24)
right_wheels(36)
accel(75.5, 0.5)
turn_straight_right(36)
#turn_left(75.5, 28, .1, 36)
straight(75.5, .75)
left_wheels(24)
straight(75.5, 1.2)

drive.stop()
servo.stop()
#GPIO.cleanup()
print('done')
