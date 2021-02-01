from pymongo import MongoClient

def dropDB_mongo(dbname):
    host = input("Enter HOST IP : ")
    user = input("Enter USER : ")
    passwd = input("Enter PASSWD : ")

    client = MongoClient(host = host, port = 9917, username = user, password = passwd)
    client.drop_database("test_db")


if __name__ == "__main__":

    dropDB_mongo("test_db")
