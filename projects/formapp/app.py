from flask import Flask, request

import sqlite3

def get_db():

    db = sqlite3.connect('app.db')

    return db

cursor = get_db().cursor()
command = """CREATE TABLE IF NOT EXISTS people(name VARCHAR, age VARCHAR)"""
cursor.execute(command)

app = Flask(__name__)

@app.get('/')
def index():
    return "App works fine"

@app.post('/receive-from-form')
def form_data():
    db = get_db()
    cursor = db.cursor()
    name = request.form.get('name')
    age = request.form.get('age')
    command = f"""INSERT INTO people(name, age) VALUES('{name}', '{age}');"""
    cursor.execute(command)
    db.commit()
    db.close()
    return f"The name is {name} and the age is {age}"

@app.post('/receive-from-json')
def json_data():
    db = get_db()
    cursor = db.cursor()
    name = request.json.get('name')
    age = request.json.get('age')
    command = f"""INSERT INTO people(name, age) VALUES('{name}', '{age}');"""
    cursor.execute(command)
    db.commit()
    db.close()
    return f"The name is {name} and the age is {age}"

@app.get('/fetch-data')
def get_all_people():
    db = get_db()
    cursor = db.cursor()
    command = """SELECT * FROM people;"""
    data = cursor.execute(command)
    print(data.fetchone())
    print(data.fetchall())
    return ""