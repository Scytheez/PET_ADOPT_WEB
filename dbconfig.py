import mysql.connector
import os
import base64

class conn:
    def __init__(self):
        try:
            self.db_conn = mysql.connector.connect(
                host='localhost', 
                user='',                    #Change me
                password='',                #Change me
                database='PET_ADOPT_SYS'    #Change me
            )
            print('Successfully Connected to Database!')
        except Exception as e:
            print('Error: ', e)

        try:
            self.cursor = self.db_conn.cursor()
        except Exception as e:
            print('Database not Connected:', e)
    
    def del_file_in_folder(self, folder_path):
            try:
                for filename in os.listdir(folder_path):
                    file_path = os.path.join(folder_path, filename)
                    try:
                        if os.path.isfile(file_path) or os.path.islink(file_path):
                            os.unlink(file_path)
                        elif os.path.isdir(file_path):
                            os.rmdir(file_path)
                    except Exception as e:
                        print(file_path, e)
            except Exception as e:
                print(e)

    def adopt_form(self, name, lname, addr, phone, email, occu, social, bday, f_pet, living_type,
                    allergy, what_pet, live, pet_resp, pet_needs, pet_emer, pet_hour, pet_env,
                    pet_supp, no_supp, other_pet, past_pet):
        
        # Upload Image
        for filename in os.listdir('static/uploads/id'):
            file_path = os.path.join('static/uploads/id', filename)
            if os.path.isfile(file_path):
                with open(file_path, 'rb') as f:
                    id_pic = f.read()
        id_encodestring = base64.b64encode(id_pic)

        user_qry = "INSERT INTO USER(name, lname, address, phone_number, email, occupation, social_media_profile, bday, valid_id, user_type) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        self.cursor.execute(user_qry, (name, lname, addr, phone, email, occu, social, bday, id_encodestring, 'adopt'))

        pet_qry = 'INSERT INTO ADOPT_PET(first_pet, living_type, allergic, what_pet, live_with, pet_health, pet_needs, pet_emergency, pet_alone, pet_env, fam_supp, if_no_explain, other_pet, past_pet) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'
        self.cursor.execute(pet_qry, (f_pet, living_type, allergy, what_pet, live, pet_resp, pet_needs, pet_emer, pet_hour, pet_env, pet_supp, no_supp, other_pet, past_pet))

        self.db_conn.commit()

        # Delete images in upload folder
        self.del_file_in_folder('static/uploads/id')

    def rehome_form(self, pet_name, pet_age, gender, breed, ownership, type, 
                    reasons, desc_pet, vaccine, vaccine1, name,
                    age, email, occupation, soc_media, phone_num):
        
        # Upload Image
        for filename in os.listdir('static/uploads/pets'):
            file_path = os.path.join('static/uploads/pets', filename)
            if os.path.isfile(file_path):
                with open(file_path, 'rb') as f:
                    pet_pic = f.read()
        pet_encodestring = base64.b64encode(pet_pic)
        
        pet_qry = 'INSERT INTO PET(pet_name, pet_age, pet_gender, pet_breed, pet_type, description, vaccinated, vaccine_type, pet_status, picture) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'
        self.cursor.execute(pet_qry, (pet_name, pet_age, gender, breed, type, desc_pet, vaccine, vaccine1, 'available', pet_encodestring, ))

        rehome_qry = 'INSERT INTO REHOME_PET(ownership, reason) VALUES(%s, %s)'
        self.cursor.execute(rehome_qry, (ownership, reasons, ))

        # Upload Image
        for filename in os.listdir('static/uploads/id'):
            file_path = os.path.join('static/uploads/id', filename)
            if os.path.isfile(file_path):
                with open(file_path, 'rb') as f:
                    id_pic = f.read()
        id_encodestring = base64.b64encode(id_pic)

        user_qry = 'INSERT INTO USER(name, age, email, occupation, social_media_profile, phone_number, user_type, valid_id) VALUES(%s, %s, %s, %s, %s, %s, %s, %s)'
        self.cursor.execute(user_qry, (name, age, email, occupation, soc_media, phone_num, 'rehome', id_encodestring, ))

        self.db_conn.commit()

        # Delete images in upload folder
        self.del_file_in_folder('static/uploads/pets')
        self.del_file_in_folder('static/uploads/id')

if __name__ == '__main__':
    conn()