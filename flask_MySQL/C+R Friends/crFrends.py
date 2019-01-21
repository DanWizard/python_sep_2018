from flask import Flask, flash, request, render_template, redirect
from mySQLConnection import connectToMySQL
app = Flask(__name__)

@app.route('/')
def display():
	mysql = connectToMySQL('friendsdb')

	all_friends = mysql.query_db("Select * from friends")
	print(all_friends)

	return render_template('CRfriends.html', all_friends = all_friends)

@app.route('/input', methods = ['POST'])
def displayingInDB():
	mysql = connectToMySQL('friendsdb')
	query = "insert into friends (first_name, last_name, occupation, created_at, updated_at) values (%(first_name)s, %(last_name)s, %(occupation)s, NOW(), NOW());"
	data = { 
		'first_name' : request.form['first_name'],
		'last_name' : request.form['last_name'],
		'occupation' : request.form['occupation']
		}
	results = mysql.query_db(query,data)
	return redirect('/') 


if __name__ == "__main__":
	app.run(debug=True)
