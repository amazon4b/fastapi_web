from pymongo import MongoClient

# 방법1 - URI
mongodb_URI = "mongodb+srv://root:1234@amazon4b.wcfzzam.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(mongodb_URI)

# 방법2 - HOST, PORT
# client = MongoClient(host='localhost', port=27017)

db = client.ubion
data = db.user
# print(client.list_database_names())

# data.insert_one({
#     "username":"park",
#     "password":"5678"
# })

# cursor = data.find({"username":"kim"})
# print(list(cursor))

cursor_1 = data.find_one({"email":"1@namer.com"})
if cursor_1 == None:
    print("sssssss")
else:
    print(cursor_1)