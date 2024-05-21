# flask-class-cohort1-2024

Create a virtual environment option 1: `python -m venv venv`
Create a virtual environment option 2: `python -m virtualenv venv`

Activate the virtual environment - Windows - Option 1: `bash: source venv\Scripts\activate`
Activate the virtual environment - Windows - Option 2: `bash: . venv\Scripts\activate`
Activate the virtual environment - Windows - Option 3: `cmd: venv\Scripts\activate`

Activate the virtual environment - Mac - Option 1: `source venv/bin/activate`
Activate the virtual environment - Mac - Option 2: `. venv/bin/activate`

Install dependencies - One by One: `pip install flask`
Install dependencies - Multiple: `pip install flask arrow`
Install dependencies - from requirements file: `pip install -r requirements.txt`

To run our app - without debug: `flask run`
To run our app - with debug: `flask run --debug`
To run our app - one specific port: `flask run -p 5050`
To run our app - one specific port - with debug: `flask run -p 5050 --debug`