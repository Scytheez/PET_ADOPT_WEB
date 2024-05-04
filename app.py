from flask import Flask, render_template, url_for, request
from flask_sqlalchemy import SQLAlchemy

app =Flask(__name__) #to reference this file

app.config['SQLALCHEMY_DATABASE_URI'] = ''

@app.route('/rehome', methods=['GET', 'POST'])

def rehome_form():
    if request.method == 'POST':
        # Get form data
        name = request.form['name']
        age = request.form['age']
        gender = request.form['gender']
        breed = request.form['breed']
        ownership = request.form['ownership']
        type = request.form['type']
        reasons = request.form['reasons']

        # Process form data here (e.g., save to a database, send an email, etc.)

        return "Form submitted successfully!"  # A simple response, you can customize it
    return render_template('rehome.html')  # Render the form template

@app.route('/')

def index():
    return render_template('index.html')

@app.route('/dashboard')  
def dashboard():
    return render_template('dashboard.html')

@app.route('/ouranimals')  
def ouranimals():
    return render_template('ouranimals.html')


@app.route('/rehome')  
def rehome():
    return render_template('rehome.html')

@app.route('/donation')  
def donation():
    return render_template('donation.html')

@app.route('/adopt')  
def adopt():
    return render_template('adopt.html')

if __name__ == "__main__":
    app.run(debug=True)