from flask import Flask, render_template, url_for, request
from flask_sqlalchemy import SQLAlchemy
from dbconfig import conn

db_conn = conn()

app =Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = ''

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/dashboard')  
def dashboard():
    return render_template('dashboard.html')

@app.route('/ouranimals')  
def ouranimals():
    return render_template('ouranimals.html')

@app.route('/rehome', methods=['GET', 'POST'])  
def rehome():
    if request.method == 'POST':
        # Get form pet data
        pet_name = request.form['name']
        pet_age = request.form['age']
        gender = request.form['gender']
        breed = request.form['breed']
        ownership = request.form['ownership']
        type = request.form['type']
        reasons = request.form['reasons']
        desc_pet = request.form['describe']
        vaccine = request.form['Vaccinated']
        vaccine1 = request.form['vaccinated1']
        pet_pic = request.form['file']

        # Get form user data
        name = request.form['name']
        age = request.form['age']
        email = request.form['email']
        occupation = request.form['occupation']
        soc_media = request.form['social']
        phone_num = request.form['phone']
        valid_id = request.form['image']

        db_conn.rehome_form(pet_name, pet_age, gender, breed, ownership, type, 
                            reasons, desc_pet, vaccine, vaccine1, pet_pic, name,
                            age, email, occupation, soc_media, phone_num, valid_id)

    return render_template('rehome.html')

@app.route('/donation')  
def donation():
    return render_template('donation.html')

@app.route('/adopt')  
def adopt():
    if request.method == 'POST':
        # Get form applicant data
        name = request.form['Fname']
        lname = request.form['Lname']
        addr = request.form['address']
        phone = request.form['phone']
        email = request.form['email']
        occu = request.form['occupation']
        social = request.form['social']
        bday = request.form['bday']

        f_pet = request.form['f_pet']
        living_type = request.form['building']
        allergy = request.form['allergy']
        what_pet = request.form['what_pet']
        live = request.form['live']


    return render_template('adopt.html')

if __name__ == "__main__":
    app.run(debug=True)