from DataBase.BankDatabase import users_collection

class InsertUsers:
    @staticmethod
    def inscription_users(prenom, nom, email, mot_de_passe, rib):
        # Check if the email already exists
        if users_collection.find_one({'email': email}):
            print("Email déjà existant.")
            return None

        # Insert user data into the users collection
        user_data = {
            'first_name': prenom,
            'last_name': nom,
            'email': email,
            'password': mot_de_passe,
            'balance': 0,  # Assuming initial balance is 0
            'rib': rib
        }
        users_collection.insert_one(user_data)
        print("Compte créé avec succès !")
        return user_data
