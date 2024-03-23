from pymongo import MongoClient
user = 'root'
password = 'MjczMTctYmF5aXJp'
host = 'localhost'
#create the connection url
connecturl = "mongodb://{}:{}@{}:27017/?authSource=admin".format(user,password,host)

# connect to mongodb server
print("connecting to mongodb server")
connection = MongoClient(connecturl)

# select the 'training' database 
db = connection.training

# select the 'python' collection
collection = db.mongodb_glossary

# creat documents
doc1 = {"Database":"a database contains collections"}
doc2 = {"collection":"a collection stores the documents"}
doc3 = {"document":"a document contains the data in the form or key value pairs."}

# insert documents
print("Insering documents into collection")

db.collection.insert_one(doc1)
db.collection.insert_one(doc2)
db.collection.insert_one(doc3)

docs = db.collection.find()

print("Printing the documents in he collection")

for document in docs:
    print(document)

print("Closing the connection")
connection.close()