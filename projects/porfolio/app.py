from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)

app.secret_key = "thfdskhksdfsdkdnflksankfnsdnfskdl"

@app.get('/')
def homepage():
    header = "Hi, I am"
    name = "Bola Ahmed Tinubu"
    title = "President Federal Republic of Nigeria"
    dob = "16th July, 2024"
    address = "Aso Rock, Abuja, Nigeria"
    email = "bola.ahmed@tinubu.org"
    phone = "+2349012345678"

    person = {
        "header":header,
        "name":name,
        "title":title,
        "dob":dob,
        "address":address,
        "email":email,
        "phone":phone
    }
    return render_template('index.html', person=person)

@app.get('/contact')
def contact():
    return render_template('contact.html')

@app.post('/contact')
def receive_messages():
    first_name = request.form.get('firstname')
    last_name = request.form.get('lastname')
    country = request.form.get('country')
    subject = request.form.get('subject')
    session[first_name] = {
        'first_name':first_name, 'last_name':last_name, 'country':country, 'subject':subject
    }
    return redirect('/')

@app.get('/message')
def message():
    messages = dict(session)
    print(messages)
    return render_template('message.html', messages=messages)