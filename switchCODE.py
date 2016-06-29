"""
This is the epic project that was undertaken by two derps in June of 2016.
:3
"""
import RPi.GPIO as GPIO
import time

frequency = 50
neutralDc = frequency*.15
topDc = frequency * .25
botDc = frequency * .05

def readyBoard(pin, frequency):
	#sets pins to be referenced by number on the r pi
	GPIO.setmode(GPIO.BOARD)
	#set pin as an output pin 
	GPIO.setup(pin,GPIO.OUT)
	#sets pin as a pwm modulated pin at a frequency
	chosenPin = GPIO.PWM(pin, frequency)
	#returns pin
	return chosenPin

#sets pin to set to neutral position
def setNeutral(pin):
	pin.start(neutralDc)
#sets pin to set to 180 position
def set180(pin):
	pin.start(topDc)
#sets pin to set to 0 position
def set0(pin):
	pin.start(botDc)
#stops pwm 
def stopPin(pin):
	pin.stop()
#demonstrates how servo is controlled by  r pi
def trialRun(pin, frequency):
	p = readyBoard(pin, frequency)
	setNeutral(p)
	try:
		while True:
			p.ChangeDutyCycle(neutralDc)
			time.sleep(1)
			p.ChangeDutyCycle(topDc)
			time.sleep(1)
			p.ChangeDutyCycle(botDc)
			time.sleep(1)

	except KeyboardInterrupt:
		stopPin(p)
		GPIO.cleanup()

#uncomments line below to see demo
#trialRun(7, frequency)

