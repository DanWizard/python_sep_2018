from flask import Flask, redirect, request, render_template, flash, session
from mySQLConnection import connectToMySQL
import re

app = Flask(__name__)
app.secret_key = 'muhsecret'
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

@app.route('/')
def enter():
	mysql = connectToMySQL('emailverification')
	email_data = mysql.query_db("select * from data")
	return render_template("validateEmail.html")

@app.route('/check', methods = ['POST'])
def checking():
	mysql = connectToMySQL('emailverification')
	
	if not EMAIL_REGEX.match(request.form['email']):
		flash('INVALID EMAIL')
		return redirect('/')
	
	elif EMAIL_REGEX.match(request.form['email']):
		mysql = connectToMySQL('emailverification')
		echeck = mysql.query_db('select * from data;')
		for i in echeck:
			if i['email'] != request.form['email']:
				session['email'] = request.form['email']
				return redirect('/put')
			else:
				mysql = connectToMySQL('emailverification')
				flash('sorry that email has been taken')
				return redirect('/')

@app.route('/put')
def add():
	mysql = connectToMySQL('emailverification')
	data = {
	'hello': session['email']
	}

	query = "insert into data (email) values (%(hello)s);"
	results = mysql.query_db(query, data)
	return redirect('/success')

@app.route('/success')
def yay():
	mysql = connectToMySQL('emailverification')
	email_data = mysql.query_db("select * from data")
	return render_template('successfulEmail.html', email_data = email_data)
	


if __name__ == '__main__':
	app.run(debug = True)