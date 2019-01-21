from flask import Flask, redirect, request, render_template, flash
from mySQLConnection import connectToMySQL

app = Flask(__name__)
app.secret_key = 'muhsecret'

@app.route('/')
def display():
	mysql = connectToMySQL('leadnclient')
	all_data= mysql.query_db("Select * from data")

	return render_template('leadsNclients.html', all_data=all_data)

@app.route('/view', methods = ['POST'])
def yo():
	mysql = connectToMySQL('leadnclient')
	query = 'insert into data(Customer_Name) values (%(Customer_Name)s);'
	data = {
	'Customer_Name' : request.form['customer_name']
	}
	results = mysql.query_db(query,data)
	return redirect('/')


if __name__ == '__main__':
	app.run(debug = True)
