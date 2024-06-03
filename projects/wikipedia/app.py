from flask import Flask, render_template

app = Flask(__name__)

@app.get('/')
def home():
    name = "Musa"
    return render_template('home.html', name=name)

@app.get('/<nation>')
def welcome(nation):
    return render_template('home.html', name=nation)