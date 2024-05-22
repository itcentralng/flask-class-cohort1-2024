from flask import Flask, request, render_template

app = Flask(__name__, )

@app.get('/')
def index():
    return render_template('index.html')

@app.post('/')
def post_data():
    data = request.form
    name = data.get('name')
    age = data.get('age')
    height = data.get('height')
    return render_template('index2.html', name=name, age=age, height=height)