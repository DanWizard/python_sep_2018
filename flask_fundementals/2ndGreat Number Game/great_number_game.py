from flask import Flask, render_template, redirect, session, request
import random

app = Flask(__name__)

app.secret_key = 'muhsecret'

@app.route('/')

def genNum():
	if 'num' not in session:
		session['num'] = int(random.randrange(1,101))
	if 'numGuess' not in session:
		session['numGuess'] = 0
	print(session['num'])
	return render_template('numgame.html')

@app.route('/processNumber', methods = ['POST'])

def process():
	session['numGuess'] = int(request.form['guess'])
	return redirect('/')

if __name__ == '__main__':
	app.run(debug = True)