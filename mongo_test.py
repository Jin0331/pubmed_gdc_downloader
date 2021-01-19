import pymongo
print(pymongo.__version__) # 3.10.1

conn = pymongo.MongoClient(host='210.115.229.80', port=9917, \
                           username='root',
                           password='sempre813!',)

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