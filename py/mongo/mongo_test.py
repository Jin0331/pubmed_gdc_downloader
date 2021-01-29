import pymongo
print(pymongo.__version__) # 4.4.3

host = input("Enter Host IP :")
passwd = input("Enter PASSWORD :")

conn = pymongo.MongoClient(host= host, port = 9917, \
                           username='root',
                           password=passwd)

str_database_name = 'test_db'
db = conn.get_database(str_database_name)

str_collection_name = 'test_table'
db.drop_collection(str_collection_name) 
collection = db.get_collection(str_collection_name)

collection.insert_one({'name': 'Trump', 'age': 70}) 
collection.insert_one({'name': 'Obama', 'age': 60}) 

results = collection.find({"age": {"$gte": 70}})
for result in results:
    print(result)  

results = collection.find({"age": {"$gte": 60}})
for result in results:
    print(result)

    