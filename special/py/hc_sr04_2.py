import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

TRIG = 8
ECHO = 10

GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)



try:
	while True:
		GPIO.output(TRIG, False)
		time.sleep(2) # waiting for sensor to settle

		#Trig Start
		GPIO.output(TRIG, True)
		time.sleep(0.00001)
		GPIO.output(TRIG, False)

		while GPIO.input(ECHO) == 0:
			pulse_start = time.time()

		while GPIO.input(ECHO) == 1:
			pulse_end = time.time() # connect to echo pin

		print "connect to echo pin" 
		pulse_duration = pulse_end - pulse_start

		distance = pulse_duration * 17150
		distance = round(distance, 2)

		print "Distance: ", distance, "cm"
except KeyboardInterrupt:
	GPIO.cleanup() 
