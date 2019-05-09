import time
import RPi.GPIO as GPIO
import csv
import nfc

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

Lock = 100
Unlock = 185

R=4#RED
G=3#GREEN
B=2#BLUE

GPIO.setup(R,GPIO.OUT)
GPIO.setup(G,GPIO.OUT)
GPIO.setup(B,GPIO.OUT)
time.sleep(1)

def led(color):
	color-=2
	GPIO.output(color+2,False)
	GPIO.output((color+1)%3+2,True)
	GPIO.output((color+2)%3+2,True)

def Servo(servoChannel, position):
	servoStr = "%d=%d\n"% (servoChannel, position)
	with open("/dev/servoblaster", "wb") as f:
		f.write(servoStr)

def verify(tag):
	v = False
	with open('data.csv', 'r') as f:
		reader = csv.reader(f)
		for row in reader:
			if str(tag) == ''.join(row):
				v = True
				break
			else:
				continue
	f.close()

	if v:
		print "OK"
	else:
		print "Wrong"



def main():

	while True:
		try:
			clf = nfc.ContactlessFrontend('usb')
			clf.connect(rdwr={'on-connect': verify}) # now touch a tag
			clf.close()			
		except KeyboardInterrupt:
			pass
			GPIO.cleanup()	
	time.sleep(0.05)

def test():
	clf = nfc.ContactlessFrontend('usb')
	clf.connect(rdwr={'on-connect': verify}) # now touch a tag
	clf.close()


if __name__ == '__main__':
	main()
	#test()
	
