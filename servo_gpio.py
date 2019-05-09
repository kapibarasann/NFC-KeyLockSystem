import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

gp_out = 17
GPIO.setup(gp_out, GPIO.OUT)

servo = GPIO.PWM(gp_out, 50)

wait = 4

servo.start(0)

servo.ChangeDutyCycle(5)
time.sleep(wait)

servo.ChangeDutyCycle(10)
time.sleep(wait)

servo.ChangeDutyCycle(5)
time.sleep(wait)

servo.ChangeDutyCycle(10)
time.sleep(wait)

servo.stop()

GPIO.cleanup()
