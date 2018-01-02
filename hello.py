from flask import Flask
from flask import redirect
from flask.ext.script import Manager
from flask import request
from flask import make_response

app = Flask(__name__)
manager = Manager(app)


#@app.route('/')
#def index():
	#return '<h1>Hello World!</h1>'
#	return redirect('https://www.baidu.com')
@app.route('/')
def index():
	response = make_response('<h1>This document carries a cookie!</h1>')
	response.set_cookie('answer', '42')
	return response

@app.route('/user/<name>')
def user(name):
	return '<h1>Hello,%s!</h1>' % name

if __name__ == '__main__':
	#app.run(host='0.0.0.0',debug=True)
	manager.run()


