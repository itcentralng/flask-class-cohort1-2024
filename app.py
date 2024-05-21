# Step 1 - is to import the Flask class from the flask module
from flask import Flask

# Step 2 - Create an app with the class - that is create an instance of the class Flask
# We need to create a variable to hold the instance of the Flask class
# We need to pass it the name of our app file using the __name__ variable
app = Flask(__name__)

# Step 3 - Create routes or endpoints that will be available on the browser
# Each endpoints starts with @ followed by the name of our variable or instance
# Followed by .Method ['GET', 'POST', 'PUT', 'DELETE', 'PATCH']
# Followed by paranthesis within which we define our endpoint e.g. '/test'

# Then under it, we pass a function that will be called each time our endoint is reached from the browser
@app.get('/')
def index():
    return "My name is Kundil"

@app.get('/age')
def age():
    return "I am 10 years old"