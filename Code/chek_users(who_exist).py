from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')
db = client['bank_system']
users_collection = db['users']


all_users = users_collection.find()


for user in all_users:
    print(user)
