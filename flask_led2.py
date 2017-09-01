import RPi.GPIO as GPIO 
from flask import Flask
#/usr/lib/python2.7/dist-packages/flask
LED = 16

app = Flask(__name__) #make instance
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(LED, GPIO.OUT,initial=GPIO.LOW)


@app.route('/')
def index():
	return 'This is the Homepage'


@app.route('/LED/<flag>')
def led(flag):
	if  flag == "ON":
		GPIO.output(LED,GPIO.HIGH)
         
	elif flag == "OFF":
		GPIO.output(LED,GPIO.LOW)


	return 'LED %s' % flag


if __name__ == "__main__":
	app.run(debug=True, host='0.0.0.0',port=8888)

