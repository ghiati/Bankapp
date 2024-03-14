from pymongo import MongoClient #nous avons besoin mosieur de Pymongo pour faire la connection entre python et mongo db 


client = MongoClient('mongodb://localhost:27017/')
db = client['bank_system']  
users_collection = db['users'] 
historique_collection = db['historique']  
