from flask import Flask, render_template

app = Flask(__name__)

print(__name__)

@app.route('/')

def defaultCheck():
	return render_template('default_checkerboard.html')

@app.route('/<num1>/<num2>')

def flexCheck(num1,num2):
	return render_template("flex_checkerboard.html", num1 = int(num1) , num2 = int(num2))

if __name__ == '__main__':
	app.run(debug = True)




