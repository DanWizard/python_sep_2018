from flask import Flask, render_template

app = Flask(__name__)

print(__name__)


@app.route('/')


def hello_world():
	return 'welcome'

@app.route('/play')

def blue():
	return render_template('playground1.html')

@app.route('/play/<times>')

def blueNum(times):

	return render_template('playground2.html', times = int(times))

@app.route('/play/<times>/<color>')

def colorNum(times, color):

	return render_template('playground3.html', times = int(times), color = color )

if __name__ == '__main__':
	app.run()
