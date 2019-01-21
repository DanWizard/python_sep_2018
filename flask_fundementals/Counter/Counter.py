from flask import Flask, redirect, request, render_template,session

app = Flask(__name__)

app.secret_key= 'ThisIsSecret'

print(__name__)

@app.route('/')

def visits():
	if 'count' not in session: 
		session['count'] = 1
	else:
		session['count'] += 1

	return render_template('counter.html', count=session['count'])

@app.route('/button', methods = ['POST'])

def iterater():
	
	return redirect('/')

@app.route('/buttonreset', methods = ['POST'])
def nuke():
	session['count'] = 0
	
	return redirect('/')

@app.route('/buttondecrease', methods = ['POST'])
def decrementer():
	session['count'] += -2
	
	return redirect('/')






if __name__ == '__main__':
	app.run(debug=True)

