from flask import Flask, render_template, redirect

app = Flask(__name__)

print(__name__)

@app.route('/play')

def show():
	return render_template('playground.html')

@app.route('/play/<num>')

def display(num):
	return render_template('playground2.html', num = int(num))

@app.route('/play/<num>/<color>')

def displayWithColor(num, color):
	return render_template('playground3.html', num = int(num), color = color)

if __name__ == '__main__':
	app.run(debug=True)