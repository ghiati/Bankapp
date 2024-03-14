from pymongo import MongoClient #on va utilise mongo db pour stoque les information de l'utilisateur 


client = MongoClient('mongodb://localhost:27017/')
db = client['bank_system']  
users_collection = db['users'] 
historique_collection = db['historique']  
