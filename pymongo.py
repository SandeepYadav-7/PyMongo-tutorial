import pymongo

client = pymongo.MongoClient("Your connection string")

# making a database

# db = client.db_name
db = client.test

# now, makig a collection,
# collection is just like a table in sql
# collection = db.create_collection("MyCol")

# now, collection has been created first time, so if we run this file second time, so we get an error msg that we have created that collection.
# and also note that, collection names are unique in a database
# means that you cannot make two different collections with the same name

# if collection is already exists
# collection = db.collection_name

collection = db.MyCol

# print(db.list_collection_names())

# now making a document
# document is just like a data in our collection
data = {
    "name": "Sandeep",
    "guild_id": 1234,
    "suggestion_channel": 1234,
    "is_suggestion_enable": True
}

# <=== collection methods ===>

# For inserting the data
# collection.insert_one(data)
# collection.insert_many() # pass a list inside this.

# For finding a record or multiple records
# collection.find_one() # pass a query inside this
# collection.find() # to find all records

# For deleting a document (data)
# collection.delete_one()
# collection.delete_ many()

# For updating a value in a document
# collection.update_one()
# collection.update_many()

# replacing (updating) a document
# collection.replace_one(finding_query, replce_some_content)

# Some Examples:-
"""
# 1

search_query = {"name": "Sandeep"}
new_data = {"$set": {"guild_id": 5555}}

collection.update_one(search_query, new_data)


# 2

collection.replace_one(
  {"name": "Sandeep"},
  {"guild_id": 9876}
)
"""

print(client)
print(collection)