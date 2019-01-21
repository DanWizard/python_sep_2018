from flask import Flask, render_template, redirect, request

app = Flask(__name__)

print(__name__)

@app.route('/')

def display():
	return "Hello World"

@app.route('/dojo')

def say():
	return "dojo"

@app.route('/say/<name>')
def say2(name):
	return 'Hi '+str(name)

@app.route('/repeat/<num>/<word>')
def say3(num, word):
	return str(word)*int(num)



if __name__ == '__main__':
	app.run(debug=True)