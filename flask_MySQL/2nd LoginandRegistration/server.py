from flask import Flask, redirect, request, render_template, flash, session
import re
from mysqlconnection import connectToMySQL
from flask_bcrypt import Bcrypt
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

app = Flask(__name__)
bcrypt = Bcrypt(app)
app.secret_key = 'muhsecrect'

@app.route('/')
def display():
	return render_template('display.html')

@app.route('/process', methods=['POST'])
def process():
		
		session['status'] = 'valid'

		mysql = connectToMySQL('loginreg')
		echeck = mysql.query_db('select * from users;')
		for i in echeck:
			if i['Email'] == request.form['email']:
				flash(u'email already used', 'email')
				session['status'] = 'invalid'
			# if i['Email'] == request.form['login_email'] and bcrypt.check_password_hash(i['Password'], request.form['login_password']):
			# 	flash(u'gg','email')

		if len(request.form['email']) < 1:
			flash(u'email cannot be empty','email')
			session['status'] = 'invalid'
		if not EMAIL_REGEX.match(request.form['email']):
			flash(u'email does not have correct form', 'email')
			session['status'] = 'invalid'

		if len(request.form['first_name']) < 1:
			flash(u'first_name cannot be empty','first_name')
			session['status'] = 'invalid'

		if len(request.form['last_name']) < 1:
			flash(u'last_name cannot be empty','last_name')
			session['status'] = 'invalid'

		if len(request.form['password']) < 1:
			flash(u'password cannot be empty','password')
			session['status'] = 'invalid'
		if request.form['password'] != request.form['confirm_password']:
			flash(u'passwords must match','password')
			session['status'] = 'invalid'

		if len(request.form['confirm_password']) < 1:
			flash(u'confirm_password cannot be empty','confirm_password')
			session['status'] = 'invalid'

		
		if session['status'] == 'valid':
			pw_hash = bcrypt.generate_password_hash(request.form['password'])
			mysql = connectToMySQL('loginreg')
			data = {
			'email': request.form['email'],
			'first_name': request.form['first_name'],
			'last_name': request.form['last_name'],
			'password': pw_hash

			}
			session['email'] = request.form['email']
			query = 'INSERT INTO users (Email, First_Name, Last_Name, Password, created_at, updated_at ) value (%(email)s, %(first_name)s, %(last_name)s, %(password)s, NOW(), NOW());'
			mysql = connectToMySQL('loginreg')
			new_user = mysql.query_db(query,data)

		return redirect('/')
@app.route('/processlogin', methods = ['POST'])
def check():
	session['status'] = 'valid'
	mysql = connectToMySQL('loginreg')
	echeck = mysql.query_db('select * from users;')
	for i in echeck:
		if i['Email'] == request.form['login_email'] and not bcrypt.check_password_hash(i['Password'], request.form['login_password']):
				flash(u'password is incorrect','email')
				session['status'] = 'invalid'

	if len(request.form['login_password']) < 1:
			flash(u'login_password cannot be empty','login_password')
			session['status'] = 'invalid'
	if len(request.form['login_email']) < 1:
			flash(u'login_email cannot be empty','login_email')
			session['status'] = 'invalid'
	if not EMAIL_REGEX.match(request.form['login_email']):
			flash(u'login_email does not have correct form', 'login_email')
			session['status'] = 'invalid'
	if session['status'] == 'valid':
		return redirect('/success')

	else:
		return redirect('/')

if __name__ == '__main__':
	app.run(debug = True)