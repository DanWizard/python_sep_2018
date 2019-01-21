from flask import Flask, render_template, redirect, request, session
from mysqlconnection import connectToMySQL
app = Flask(__name__)
@app.route('/')
def display():
	return render_template('display.html')
	

if __name__ == "__main__":
    app.run(debug=True)