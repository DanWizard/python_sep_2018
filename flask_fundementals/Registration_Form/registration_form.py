from flask import flash, Flask, render_template, redirect, request
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
app = Flask(__name__)
app.secret_key = 'muhsecret'

@app.route('/')
def render():
	return render_template('registration.html')

@app.route('/validate', methods = ['POST'])
def validate():
	for i in request.form['first_name']:
		if i >= '0' and i <= '9':
			flash("First Name cannot contain numbers")
			break

	for i in request.form['last_name']:
		if i >= '0' and i <= '9':
			flash("Last Name cannot contain numbers")
			break

	if len(request.form['email']) < 1:
		flash("email cannot be empty")

	if not EMAIL_REGEX.match(request.form['email']):
		flash("Invalid Email Address!")

	if len(request.form['first_name']) < 1:
		flash("first_name cannot be empty")

	if len(request.form['last_name']) < 1:
		flash("last_name cannot be empty")

	if len(request.form['password']) < 1:
		flash("password cannot be empty")

	if len(request.form['password']) > 8:
		flash("password cannot be larger than 8 characters")

	if len(request.form['confirm_password']) < 1:
		flash("confirm_password cannot be empty")

	if request.form['password'] != request.form['confirm_password']:
		flash("passwords must match")

	
	print(request.form['password'])
	print(request.form['confirm_password'])
	return redirect('/')



if __name__ == '__main__':
	app.run(debug=True)
