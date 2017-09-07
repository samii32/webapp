import RPi.GPIO as GPIO
from DHT11_Python.dht11 import DHT11
import httplib, urllib
import time
import Adafruit_DHT


sensor= Adafruit_DHT.DHT11
pin = 14

KEY = 'WJ6NEYE2FO0G0HVA'
headers = {"Content-type":"application/x-www-form-urlencoded","Accept":"text/plain"}

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.cleanup()



def dht11_read():
	
	humidity,temperature = Adafruit_DHT.read_retry(sensor, pin)

	if temperature is not None:
    		print('Temp={0:0.1f}*C  '.format(temperature))
	 	temperature  = temperature

	else:
		print('Failed to get reading. Try again!')
		temperature = 0.0
	
	return temperature
while True:
	temp = dht11_read()
	params = urllib.urlencode({'field1': temp, 'key':KEY })
	conn = httplib.HTTPConnection("api.thingspeak.com:80")
	try:
		conn.request("POST","/update",params, headers)
		response = conn.getresponse()
		print response.status, response.reason
		print "success"
	except:
		print "Connection failed"
	time.sleep(5)
