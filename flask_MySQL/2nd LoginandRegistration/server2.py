from flask import Flask, render_template, redirect, request, session, flash
from mysqlconnection import connectToMySQL
from flask_bcrypt import Bcrypt
import re, datetime
from datetime import *
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
NAME_REGEX = re.compile(r'^[a-zA-Z]+$')

app = Flask(__name__)
app.secret_key = 'huh'
bcrypt = Bcrypt(app)

@app.route('/')
def index():
    mysql = connectToMySQL("friendsdb")
    query = 'SELECT * FROM friends;'
    users = mysql.query_db(query)
    print("all users", users)
    return render_template('index.html')

@app.route('/createUser', methods=['Post'])
def process():

    if len(request.form['first_name']) < 2:
        flash('First Name Required', 'first_name')
    elif not NAME_REGEX.match(request.form['first_name']):
        flash('First Name cannot contain numbers or symbols', 'first_name')

    if len(request.form['last_name']) < 2:
        flash('Last Name Required', 'last_name')
    elif not NAME_REGEX.match(request.form['last_name']):
        flash('Last Name cannot contain numbers', 'last_name')

    if len(request.form['email']) <1:
        flash('Email cannot be blank!', 'email')
    elif not EMAIL_REGEX.match(request.form['email']):
        flash('Invalid Email Address!', 'email')
    mysql = connectToMySQL("friendsdb")
    query = "SELECT email FROM friends;"
    all_emails = mysql.query_db(query)
    print("Fetched all emails", all_emails)
    for email in all_emails:
        if request.form['email'] == email['email']:
            flash('Email already in database', 'email')

    if len(request.form['password']) < 8:
        flash('Password must be at least 8 characters', 'password')
    if not re.search('[A-Z]', request.form['password']):
        flash('Password must contain at least one capital letter', 'password')
    if not re.search('[0-9]', request.form['password']):
        flash('Password must contain at least one number', 'password')
    elif request.form['password'] != request.form['passconfirm']:
        flash('Passwords do not match', 'password')
    
    if '_flashes' in session.keys():
        return redirect('/')
    else:

        pwd = bcrypt.generate_password_hash(request.form['password'])
        print(pwd)
        mysql = connectToMySQL('friendsdb')
        query = 'INSERT INTO friends(first_name, last_name, email, password, created_at, updated_at) VALUES (%(first_name)s, %(last_name)s, %(email)s, %(password)s, NOW(), NOW());'
        data = {
            'first_name': request.form['first_name'],
            'last_name': request.form['last_name'],
            'email': request.form['email'],
            'password': pwd
        }
        newuser = mysql.query_db(query, data)
        print(newuser)
        flash('You have been successfully registered', 'success')
        if newuser not in session:
            session['userid'] = newuser
            session['name'] = request.form['first_name']
        return redirect('/success')

@app.route('/success')
def success():
    if 'userid' not in session:
        return redirect('/')
    return render_template('success.html')

@app.route('/login', methods=['POST'])
def login():
    mysql = connectToMySQL('friendsdb')
    query = 'SELECT * FROM friends WHERE email = %(email)s;'
    data = {
            'email': request.form['username'],
        }
    result = mysql.query_db(query, data)
    if result:
        if bcrypt.check_password_hash(result[0]['password'], request.form['pw']):
            session['userid'] = result[0]['id']
            session['name'] = result[0]['first_name']
            return redirect ('/success')
    flash('You could not be logged in')
    return redirect('/')


@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')

    
    
if __name__=="__main__":
    app.run(debug=True)