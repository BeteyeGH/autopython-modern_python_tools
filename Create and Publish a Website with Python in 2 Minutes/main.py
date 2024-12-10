from flask import Flask

app = Flask(__name__)

@app.route('/') #starting with homepage
def home():
    return "Welcome to the website!"

@app.route('/name=<name>-lastname=<last>') #you can then add extra pages with extensions provided
def my_view_func(name, last): #the function you've defined's return gets shown on the page path
    name_fixed = name.title()
    last_fixed = last.title()
    return (f"Name is {name_fixed}\nLast name is {last_fixed}.")

app.run() #running the app