from flask import Flask, request

app = Flask(__name__) #make instance
@app.route('/')
def index():
	return 'Method used: %s' % request.method
	#get or post
@app.route('/bacon', methods=['GET','POST'])
def bacon():
	if request.method == 'POST':
		return 'You are using POST'
	else:
		return 'You are probably using GET'

if __name__ == "__main__":
	app.run(debug=True, host='0.0.0.0', port=8888)
