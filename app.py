from flask import Flask, render_template, request
from dbconfig import conn
import os
from werkzeug.utils import secure_filename
<<<<<<< HEAD
from flask import Flask, render_template, request
from knn_model import knn_classifier, vectorizer



=======
from knn_model import knn_classifier, vectorizer

>>>>>>> bc196a921fccea737c5fd930710533a3050f82b3
app =Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

db_conn = conn()

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/dashboard')  
def dashboard():
    return render_template('dashboard.html')

<<<<<<< HEAD
@app.route('/ouranimals')  
=======
@app.route('/ouranimals')
>>>>>>> bc196a921fccea737c5fd930710533a3050f82b3
def ouranimals():
    db_conn = conn()

    items_per_page = 10
    page = int(request.args.get('page', 1))

    offset = (page - 1) * items_per_page

    query = f"SELECT pet_name, pet_age, pet_gender, pet_breed, picture FROM PET WHERE pet_status = 'available' LIMIT {items_per_page} OFFSET {offset}"
    db_conn.cursor.execute(query)
    pets = db_conn.cursor.fetchall()


    query = f"SELECT COUNT(*) FROM PET WHERE pet_status = 'available'"
    db_conn.cursor.execute(query)
    total_pets = db_conn.cursor.fetchone()[0]

    has_next = (offset + items_per_page) < total_pets

    db_conn.cursor.close()
    db_conn.db_conn.close() 

    return render_template('ouranimals.html', pets=pets, page=page, has_next=has_next)

@app.route('/rehome', methods=['GET', 'POST'])  
def rehome():
    if request.method == 'POST':
        try:
            # Get form pet data
            pet_name = request.form['pet_name']
            pet_age = request.form['pet_age']
            gender = request.form['gender']
            breed = request.form['breed']
            ownership = request.form['ownership']
            type = request.form['type']
            reasons = request.form['reasons']
            desc_pet = request.form['describe']
            vaccine = request.form['Vaccinated']
            vaccine1 = request.form['vaccinated1']

            pet_pic = request.files.get('file')
            pet_pic_path = None 
            if pet_pic and allowed_file(pet_pic.filename):
                filename = secure_filename(pet_pic.filename)
                pet_pic_path = os.path.join('static/uploads/pets', filename)
                pet_pic.save(pet_pic_path)

            # Get form user data
            name = request.form['name']
            age = request.form['age']
            email = request.form['email']
            occupation = request.form['occupation']
            soc_media = request.form['social']
            phone_num = request.form['phone']
            
            valid_id = request.files.get('image')
            valid_id_path = None
            if valid_id and allowed_file(valid_id.filename):
                filename = secure_filename(valid_id.filename)
                valid_id_path = os.path.join('static/uploads/id', filename)
                valid_id.save(valid_id_path)

            db_conn.rehome_form(pet_name, pet_age, gender, breed, ownership, type, 
                                reasons, desc_pet, vaccine, vaccine1, name,
                                age, email, occupation, soc_media, phone_num)
            
        except Exception as e:
            print(e)

    return render_template('rehome.html')

@app.route('/donation')  
def donation():
    return render_template('donation.html')

<<<<<<< HEAD

=======
>>>>>>> bc196a921fccea737c5fd930710533a3050f82b3
@app.route('/predictor', methods=['GET', 'POST'])
def predictor():
    if request.method == 'POST':
        try:
            # Get selected traits from the form
            selected_traits = request.form.getlist('describe')

            # Predict pet attitudes based on the selected traits
            predicted_probabilities = knn_classifier.predict_proba(vectorizer.transform([' '.join(selected_traits)]))[0]
            predicted_pet_attitudes = knn_classifier.classes_

            # Prepare data to display on webpage
            results = []
            for attitude, probability in zip(predicted_pet_attitudes, predicted_probabilities):
                results.append({'attitude': attitude, 'probability': probability})

            return render_template('prediction_result.html', results=results)

        except Exception as e:
            error_message = "An error occurred: " + str(e)
            return render_template('error.html', error_message=error_message)

    else:
        return render_template('predictor.html')

@app.route('/adopt', methods=['GET', 'POST'])  
def adopt():
    if request.method == 'POST':
        try:
            # Get form applicant data
            name = request.form['Fname']
            lname = request.form['Lname']
            addr = request.form['address']
            phone = request.form['phone']
            email = request.form['email']
            occu = request.form['occupation']
            social = request.form['social']
            bday = request.form['bday']

            f_pet = request.form['firsttime']
            living_type = request.form['building']
            allergy = request.form['allergic']
            what_pet = request.form['what_pet']
            live = request.form['live']

            pet_resp = request.form['pet_resp']
            pet_needs = request.form['pet_needs']
            pet_emer = request.form['pet_emer']
            pet_hour = request.form['pet_hour']
            pet_env = request.form['pet_env']
            pet_supp = request.form['pet_supp']
            no_supp = request.form['not_supp']
            other_pet = request.form['other_pet']
            past_pet = request.form['past_pet']

            valid_id = request.files.get('file')
            valid_id_path = None
            if valid_id and allowed_file(valid_id.filename):
                filename = secure_filename(valid_id.filename)
                valid_id_path = os.path.join('static/uploads/id', filename)
                valid_id.save(valid_id_path)

            db_conn.adopt_form(name, lname, addr, phone, email, occu, social, bday, f_pet, living_type,
                            allergy, what_pet, live, pet_resp, pet_needs, pet_emer, pet_hour, pet_env,
                            pet_supp, no_supp, other_pet, past_pet)
        except Exception as e:
            print(e)

    return render_template('adopt.html')

<<<<<<< HEAD


if __name__ == "__main__":
    app.run(debug=True)

=======
if __name__ == "__main__":
    app.run(debug=True)
>>>>>>> bc196a921fccea737c5fd930710533a3050f82b3
