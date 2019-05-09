from subprocess import call
import time

Lock = 100
Unlock = 185

call(["sudo servod --p1pins=7"], shell=True)

def Servo(c, p):

#	call(["sudo servod --p1pins=11"], shell=True)
#	time.sleep(1)

	str = "%d=%d\n"% (c, p)
	with open("/dev/servoblaster", "wb") as f:
		f.write(str)
	f.close()
#	time.sleep(1)

#	time.sleep(1)


if __name__ == '__main__':
	while True:
		try:
			Servo(0, 100)
			print "set 100"
			time.sleep(3)

			Servo(0, 0)
			print "sleep"
			time.sleep(3)

			Servo(0, 200)
			print "set 185"
			time.sleep(3)

			Servo(0, 0)
			print "sleep"
			time.sleep(3)

		except KeyboardInterrupt:
			pass
			print "exit"
			call(["sudo killall servod"], shell=True)
			break
