from flask import Flask, redirect, request, render_template, session, flash
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

app = Flask('__name__')

app.secret_key = 'muhsecret'

@app.route('/')
def display():
	return render_template('regfomr.html')

@app.route('/checkData', methods = ['POST'])
def check():

	
	for i in request.form['first_name']:
		if i >= '0' and i <= '9':
			flash(u"first_name cannot contain numbers",'first_name')
			break
	for i in request.form['last_name']:
		if i >= '0' and i <= '9':
			flash(u"last_name cannot contain numbers",'last_name')
			break
	if len(request.form['last_name']) < 1:
		 lastname = flash(u"last_name cannot be blank",'last_name')
	if len(request.form['password']) < 1:
		flash(u"password cannot be blank",'password')
	if len(request.form['confirm_password']) < 1:
		flash(u"confirm_password cannot be blank",'confirm_password')
	if request.form['password'] != request.form['confirm_password']:
		flash(u"passwords must match",'password')
	if not EMAIL_REGEX.match(request.form['email']):
		flash(u"email is invalid",'email')
	if len(request.form['email'])< 1:
		flash(u"email cannot be blank",'email')
	if len(request.form['first_name']) < 1:
		flash(u"password cannot be blank",'first_name')

	print(lastname)

	return redirect('/')
if __name__ == '__main__':
	app.run(debug = True)