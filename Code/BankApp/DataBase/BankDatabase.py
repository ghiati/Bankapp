from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['bank_system']  
users_collection = db['users'] 
historique_collection = db['historique']
