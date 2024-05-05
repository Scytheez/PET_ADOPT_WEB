import mysql.connector

class conn:
    def __init__(self):
        try:
            self.db_conn = mysql.connector.connect(
                host='localhost',
                user='ubunts',
                password='Changeme#123',
                database='PET_ADOPT_SYS'
            )
            print('success')
        except Exception as e:
            print('Error: ', e)

        self.cursor = self.db_conn.cursor()

    def adopt_form(self, name, lname, addr, phone, email, occu, social, bday, f_pet, living_type,
                    allergy, what_pet, live, pet_resp, pet_needs, pet_emer, pet_hour, pet_env,
                    pet_supp, no_supp, other_pet, past_pet, valid_id):
        user_qry = "INSERT INTO USER(name, lname, address, phone_number, email, occupation, social_media_profile, bday, valid_id, user_type) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        self.cursor.execute(user_qry, (name, lname, addr, phone, email, occu, social, bday, valid_id, 'adopt'))

        pet_qry = 'INSERT INTO ADOPT_PET(first_pet, living_type, allergic, what_pet, live_with, pet_health, pet_needs, pet_emergency, pet_alone, pet_env, fam_supp, if_no_explain, other_pet, past_pet) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'
        self.cursor.execute(pet_qry, (f_pet, living_type, allergy, what_pet, live, pet_resp, pet_needs, pet_emer, pet_hour, pet_env, pet_supp, no_supp, other_pet, past_pet))

        self.db_conn.commit()
        self.cursor.close()

    def rehome_form(self, pet_name, pet_age, gender, breed, ownership, type, 
                    reasons, desc_pet, vaccine, vaccine1, pet_pic, name,
                    age, email, occupation, soc_media, phone_num, valid_id):
        pet_qry = 'INSERT INTO PET(pet_name, pet_age, pet_gender, pet_breed, pet_type, description, vaccinated, vaccine_type, picture, pet_status) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'
        self.cursor.execute(pet_qry, (pet_name, pet_age, gender, breed, type, desc_pet, vaccine, vaccine1, pet_pic, 'available'))

        rehome_qry = 'INSERT INTO REHOME_PET(ownership, reason) VALUES(%s, %s)'
        self.cursor.execute(rehome_qry, (ownership, reasons))

        user_qry = 'INSERT INTO USER(name, age, email, occupation, social_media_profile, phone_number, valid_id, user_type) VALUES(%s, %s, %s, %s, %s, %s, %s, %s)'
        self.cursor.execute(user_qry, (name, age, email, occupation, soc_media, phone_num, valid_id, 'rehome'))

        self.db_conn.commit()
        self.cursor.close()

if __name__ == '__main__':
    conn()