import  time
import RPi.GPIO as GPIO

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

GPIO.setup(17, GPIO.OUT)
GPIO.output(17, False)

def Servo(s, p):
	str = "%d=%d\n" % (s, p)
	with open("/dev/servoblaster", "wb") as f:
		f.write(str)
	f.close()

if __name__ == '__main__':
	while True:
		#GPIO.output(17, False)
		#time.sleep(0.1)
		Servo(0, 150)
		time.sleep(3)
		#GPIO.output(17, True)
		#time.sleep(3)

		#GPIO.output(17, False)
		#time.sleep(0.1)
		Servo(0, 90)
		time.sleep(3)
		#GPIO.output(17, True)
		#time.sleep(3)
