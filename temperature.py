from flask import Flask, render_template
import dht11_1 

app = Flask(__name__)

result = Result()

@app.route('/')
def index():
	return 'hi temp'


@app.route('/temp')
def articles():
	return render_template('temp.html',result=Result)


if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0', port=8888)
