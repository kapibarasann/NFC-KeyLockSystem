import time
import RPi.GPIO as GPIO

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

GPIO.setup(2,GPIO.OUT)
GPIO.setup(3,GPIO.OUT)
GPIO.setup(4,GPIO.OUT)
time.sleep(1)

GPIO.output(2,True)
GPIO.output(3,True)
GPIO.output(4,True)



if __name__ == '__main__':
	print "LED"
	time.sleep(2)
	print "Red"
	GPIO.output(2,True)
	GPIO.output(3,False)
	GPIO.output(4,True)
	time.sleep(2)

	print "clean"
	GPIO.output(2,True)
	GPIO.output(3,True)
	GPIO.output(4,True)
	time.sleep(2)

	print "Blue"
	GPIO.output(2,False)
	GPIO.output(3,True)
	GPIO.output(4,True)
	time.sleep(2)

	GPIO.cleanup()
