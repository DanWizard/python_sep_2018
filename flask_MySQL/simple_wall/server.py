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

		mysql = connectToMySQL('simplewall')
		echeck = mysql.query_db('select * from users;')
		for i in echeck:
			if i['email'] == request.form['email']:
				flash(u'email already used', 'email')

		if len(request.form['email']) < 1:
			flash(u'email cannot be empty','email')
		if not EMAIL_REGEX.match(request.form['email']):
			flash(u'email does not have correct form', 'email')

		if len(request.form['first_name']) < 1:
			flash(u'first_name cannot be empty','first_name')

		if len(request.form['last_name']) < 1:
			flash(u'last_name cannot be empty','last_name')

		if len(request.form['password']) < 1:
			flash(u'password cannot be empty','password')
		if request.form['password'] != request.form['confirm_password']:
			flash(u'passwords must match','password')

		if len(request.form['confirm_password']) < 1:
			flash(u'confirm_password cannot be empty','confirm_password')

		if not '_flashes' in session.keys():
			# print('hello')
			pw_hash = bcrypt.generate_password_hash(request.form['password'])
			mysql = connectToMySQL('simplewall')
			data = {
			'email': request.form['email'],
			'first_name': request.form['first_name'],
			'last_name': request.form['last_name'],
			'password': pw_hash

			}
			session['email'] = request.form['email']
			query = 'INSERT INTO users (email, first_name, last_name, password, created_at, updated_at ) values (%(email)s, %(first_name)s, %(last_name)s, %(password)s, NOW(), NOW());'
			new_user = mysql.query_db(query,data)
			session['user_id'] = new_user

		return redirect('/')
@app.route('/processlogin', methods = ['POST'])
def check():
	mysql = connectToMySQL('simplewall')
	data = {
	'email' : request.form['login_email']
	}

	echeck = mysql.query_db('SELECT * from users where email = %(email)s;',data)
	if echeck:
		print('jello')
		if bcrypt.check_password_hash(echeck[0]['password'], request.form['login_password']):
			session['user_id'] = echeck[0]['idUsers']
			return redirect('/home')
		else:
			flash(u'invalid login', 'login_email')
			return redirect('/')
	if not echeck:
		flash(u'invalid login', 'login_email')
		return redirect('/')

@app.route('/home')
def show():
	mysql = connectToMySQL('simplewall')
	data ={
	'id': session['user_id'] 
	}
	user_first_name = mysql.query_db('SELECT * FROM users WHERE idUsers = %(id)s;',data)
	session['user_name'] = user_first_name[0]['first_name']
	mysql = connectToMySQL('simplewall')
	other_users = mysql.query_db('SELECT * FROM users WHERE idUsers != %(id)s;', data)
	mysql  = connectToMySQL('simplewall')
	user_messages = mysql.query_db('SELECT * FROM messages JOIN users ON messages.idSender = users.idUsers WHERE idUser = %(id)s;', data)
	mysql = connectToMySQL('simplewall')
	messages_recieved = mysql.query_db('SELECT COUNT(idUser) FROM messages WHERE idUser = %(id)s;', data)
	mysql = connectToMySQL('simplewall')
	messages_sent = mysql.query_db('SELECT COUNT(idSender) FROM messages WHERE idSender = %(id)s;', data)
	print(messages_sent)


	return render_template('home.html', other_users = other_users, user_messages = user_messages, messages_recieved = messages_recieved, messages_sent = messages_sent)

@app.route('/logoff')
def wipe():
	session.clear()
	return redirect('/')

@app.route('/push/<to>', methods = ['POST'])
def push(to):
	# print('hello')
	if len(request.form['message']) < 1:
		flash(u'message empty')
		return redirect('/home')
	mysql = connectToMySQL('simplewall')
	data = {
	'reciever': to,
	'message': request.form['message'],
	'sender': session['user_id']
	}
	push = mysql.query_db('INSERT INTO messages(idUser, messages,  idSender, created_at, updated_at) VALUES (%(reciever)s, %(message)s, %(sender)s, NOW(), NOW());', data)
	return redirect('/home')

@app.route('/delete/<do>')
def remove(do):
	mysql = connectToMySQL('simplewall')
	data = {
	'message_id': int(do)
	}
	mysql.query_db('DELETE FROM messages WHERE idMessages = %(message_id)s;', data)		
	return redirect('/home')






if __name__ == '__main__':
	app.run(debug = True)