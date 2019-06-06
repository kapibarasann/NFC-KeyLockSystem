from subprocess import call
import time
import RPi.GPIO as GPIO
import csv
import nfc
import sys

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

Lock = 100
Unlock = 200

key_state = Lock
v = False

R=3 #RED
G=4 #GREEN
B=2 #BLUE

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
	f.close()


def key_move(current_state):
	if current_state == Unlock:
		Servo(0, Lock)
		next_state = Lock
		print "Locked\n"
		time.sleep(0.8)
		led(R)
		time.sleep(1)
		Servo(0, 0) #free up Servo

	elif current_state == Lock:
		Servo(0, Unlock)
		next_state = Unlock
		print "Unlocked\n"
		time.sleep(0.8)
		led(B)
		time.sleep(1)
		Servo(0, 0) #free up Servo

	return next_state

def wrong_card():
	for i in range(2):
		led(R)
		time.sleep(0.1)
		led(G)
		time.sleep(0.1)

	global key_state
	if key_state == Lock:
		led(R)
	elif key_state == Unlock:
		led(B)

def verify(tag):
	global v
	v = False
	with open('/home/pi/Key/data.csv', 'r') as f:
		reader = csv.reader(f)
		for row in reader:
			if str(tag) == ''.join(row):
				v = True
				break
			else:
				continue
	f.close()




def main():
	call(["sudo servod --p1pins=11"], shell=True)
	while True:
		try:
			print "Touch a Card"
			clf = nfc.ContactlessFrontend('usb')
			clf.connect(rdwr={'on-connect': verify}) # now touch a tag
			clf.close()

			global v
			global key_state

			if v:
				print "OK"
				key_state = key_move(key_state)
				time.sleep(1)
			else:
				print "Wrong"
				wrong_card()

		except KeyboardInterrupt:
			pass
			print "KeyboardINtturupt exit"
			Servo(0, Lock)
			call(["sudo killall servod"], shell=True)
			GPIO.cleanup()
			break

		except IOError:
			pass
			print "IOError exit"
			Servo(0, Lock)
			call(["sudo killall servod"], shell=True)
			GPIO.cleanup()
			break

	time.sleep(0.05)


if __name__ == '__main__':
	main()
