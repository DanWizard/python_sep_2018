from flask import Flask, render_template, request, redirect, session
import random

app = Flask(__name__)
app.secret_key = 'muhsecrect'



@app.route('/')
def displayHome():
	if 'farmAct' not in session:
		session['farmAct'] = []
		session['casinoAct'] = []
		session['caveAct'] = []
		session['houseAct'] = []
		session['goldSum'] = 0
	return render_template('ninja_gold.html')


@app.route('/processGold', methods = ['POST'])
def process():
	if 'farmAct' in request.form:
		gold = random.randrange(10,21)
		farmAct = session['farmAct']
		farmAct.append(gold)
		session['farmAct'] = farmAct
		session['goldSum'] += gold
		

	if 'caveAct' in request.form:
		gold = random.randrange(5,10)
		caveAct = session['caveAct']
		caveAct.append(gold)
		session['caveAct'] = caveAct
		session['goldSum'] += gold

	if 'houseAct' in request.form:
		gold = random.randrange(2,5)
		houseAct = session['houseAct']
		houseAct.append(gold)
		session['houseAct'] = houseAct
		session['goldSum'] += gold

	if 'casinoAct' in request.form:
		gold = random.randrange(random.randrange(-50,0),random.randrange(0,50))
		casinoAct = session['casinoAct']
		casinoAct.append(gold)
		session['casinoAct'] = casinoAct
		session['goldSum'] += gold
	print(session['goldSum'])
	print(gold)
	print(session['casinoAct'])
	return redirect('/')

if __name__ == '__main__':
	app.run(debug = True)