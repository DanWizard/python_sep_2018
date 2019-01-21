from flask import Flask
app = Flask(__name__)

print(__name__)

@app.route('/')

def hello_world():
    return "Hello World!"

@app.route('/Dojo')

def say_dojo():
    return "Dojo!"

@app.route('/say/<name>')

def say_name(name):

    if name == "flask":
        return 'hi flask'

    if name == "michael":
        return "hi michael"

    if name == "john":
        return "hi john"

    return "name= " +name

@app.route('/repeat/<itr>/<val>')

def num_of_repeat(itr,val):
    return str(val)*int(itr) 

if __name__  == "__main__":

    app.run()



