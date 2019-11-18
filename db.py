import pymongo



db_client = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = db_client['lisa']

usr_collection = mydb['users']

user_dict = {
    "name": "Krishna Deepak",
    "email": "deepaknk@aditya.ac.in",
    "tag": ['kimoshare'],
    "shared_ids": ['1','2','3','4','5','6','7'],
    "interested_tags": ['']
}

def insert_item(dict):
    x = usr_collection.insert_one(dict)

    return x.inserted_id

def clear_collection():
    # method to clear all items in the collection
    x = usr_collection.delete_many({})
    print (x.deleted_count, "items deleted")

#x = usr_collection.insert_one(user_dict)

#print (x.inserted_id)

def find_item(key, value):
    query = {key : value}
    x = usr_collection.find_one(query)

    return x


if __name__ == "__main__":
    clear_collection()
    insert_item(user_dict)
    item = find_item('name', 'Krishna Deepak')
    for x in item['shared_ids']:
        print(x)