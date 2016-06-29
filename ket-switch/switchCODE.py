"""
This is the epic project that was undertaken by two derps in June of 2016.
:3
"""
import RPi.GPIO as GPIO
import time

#sets pins to be referenced by number on the r pi
GPIO.setmode(GPIO.BOARD)
#set pin 7 as an output pin 
GPIO.setup(7,GPIO.OUT)
#sets pin 7 as a pwm modulated pin
chosenPin7 = GPIO.PWM(7, 50)
#sets pin to set to neutral position
def setNeutral(pin):
	pin.start(7.5)
#sets pin to set to 180 position
def set180(pin):
	pin.start(12.5)
#sets pin to set to 0 position
def set0(pin):
	pin.start(2.5)
#stops pwm 
def stopPin(pin):
	pin.stop()
#demonstrates how servo is controlled by  r pi
def trialRun(pin):
	setNeutral(pin)
	try:
		while True:
			pin.ChangeDutyCycle(7.5)
			time.sleep(1)
			pin.ChangeDutyCycle(12.5)
			time.sleep(1)
			pin.ChangeDutyCycle(2.5)
			time.sleep(1)

	except KeyboardInterrupt:
		stopPin(pin)
		GPIO.cleanup()

trialRun(chosenPin7)

