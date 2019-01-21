from flask import Flask, render_template, request, redirect, flash


app = Flask(__name__)

print(__name__)
app.secret_key='muhsecret'
@app.route('/')

def formInput():
	return render_template('survey.html')

@app.route('/data', methods = ['POST'])
def dataView():
	print('harvested data')
	name = request.form['name']
	email = request.form['email']
	if len(request.form['name']) < 1:
		flash('oy mate, need an input')
	else:
		flash(f"CONGRATS! your name is "+name)
	if len(request.form['name']) > 120:
		return redirect('/nowhere')

	if len(request.form['email']) < 1:
		flash('oy mate, need an input for dis email')
	else:
		flash(f"CONGRATS! your name is "+email)




	return redirect('/')

	# return render_template('dataFromSurvey.html', name= name, email=email)

@app.route('/danger')
def showInConsole():
	print("danger.....")
	return None

if __name__ == '__main__':
	app.run(debug = True)