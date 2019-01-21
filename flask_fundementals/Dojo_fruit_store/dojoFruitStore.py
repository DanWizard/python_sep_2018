from flask import Flask, redirect, request, render_template

app = Flask(__name__)

print(__name__)

@app.route('/')

def buyStuff():
	return render_template('store.html')

@app.route('/checkout', methods = ['POST'])

def showStuffBought():
	strawberry = int(request.form['strawberry'])
	rasberry = int(request.form['rasberry'])
	apple = int(request.form['apple'])
	name = request.form['name']
	studentID = request.form['StudentID']
	value = int(request.form['strawberry'])+int(request.form['rasberry'])+int(request.form['apple'])

	return render_template('storedData.html' , value= value, strawberry=strawberry, rasberry=rasberry, apple=apple, name=name, studentID=studentID)






if __name__ == '__main__':
	app.run(debug=True)
