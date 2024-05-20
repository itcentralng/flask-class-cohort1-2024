from flask import Flask

app = Flask(__name__)

@app.get('/')
def index():
    return "My name is Kundil"

@app.get('/age')
def age():
    return "I am 10 years old"