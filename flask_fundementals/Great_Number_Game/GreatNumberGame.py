from flask import Flask, render_template, request, redirect, session
import random

app = Flask(__name__)
app.secret_key = 'Thisismysecret'

@app.route('/')
def createRandom():
	if 'num' not in session:
		session['num'] = int(random.randrange(1,101))
		print(session['num'])
	if 'numGuess' not in session:
		session['numGuess'] = 0


	return render_template('GreatNumberGame.html')

@app.route('/storednumber', methods = ['POST']  )
def storeGuess():
	session['numGuess'] = int(request.form['numGuess'])

	print (session['numGuess'])

	return redirect('/')
@app.route('/youwin', methods = ['POST'])
def removeSession():
	session.clear()

	return redirect('/')





if __name__ == '__main__':
	app.run(debug = True)


