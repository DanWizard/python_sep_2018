from flask import Flask, render_template, redirect, request, session
from mysqlconnection import connectToMySQL
app = Flask(__name__)

@app.route('/')
def display():
	mysql = connectToMySQL('crfriends')
	all_friends = mysql.query_db('SELECT * from friends')
	print(all_friends)
	return render_template('home.html', all_friends = all_friends)

@app.route('/process', methods = ['POST'])
def process():
	mysql = connectToMySQL("crfriends")
	query = "insert into friends (First_Name, Last_Name, Occupation) values (%(first_name)s, %(last_name)s, %(occupation)s)"
	data = {
	'first_name' : request.form['first_name'],
	'last_name' : request.form['last_name'],
	'occupation' : request.form['occupation']
	}
	new_friend_id = mysql.query_db(query, data)
	print(new_friend_id)
	return redirect('/')


if __name__ == "__main__":
    app.run(debug=True)