from flask import Flask, render_template, redirect, request, session
import random

app = Flask(__name__)
app.secret_key = "muhsecret"


@app.route('/')
def frontpage():
	if 'farmAction' not in session:
		
		session['farmAction'] = []
		session['caveAction'] = []
		session['houseAction'] = []
		session['casinoAction'] = []
		session['accumulate'] = 0
	print(session['farmAction'])
	
	return render_template('ninjaGold.html')

@app.route('/getgold', methods = ['POST'])

def accumulate():
	if 'farmGold' in request.form:
		gold = random.randrange(10,20)
		farmAct = session['farmAction']
		farmAct.append(gold)
		session['farmAction'] = farmAct
		session['accumulate'] += gold 
			
		print(session['farmAction'])

	if 'caveGold' in request.form:
		gold = random.randrange(5,10)
		caveAct = session['caveAction']
		caveAct.append(gold)
		session['caveAction'] = caveAct
		session['accumulate'] += gold 
		print(session['caveAction'])
	


	if 'houseGold' in request.form:
		gold = random.randrange(2,5)
		houseAct = session['houseAction']
		houseAct.append(gold)
		session['houseAction'] = houseAct
		session['accumulate'] += gold 
		print(session['houseAction'])

	if 'casinoGold' in request.form:
		gold = random.randrange(-50,50)
		casinoAct = session['casinoAction']
		casinoAct.append(gold)
		session['casinoAction'] = casinoAct
		session['accumulate'] += gold 
		print(session['casinoAction'])
	
	return redirect('/')

if __name__ == '__main__':
	app.run(debug=True)
	

