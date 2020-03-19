from pymongo import MongoClient

client = MongoClient()
db = client.pegasus
counters = db.counters
teachers = db.teachers
classes = db.classes
null_counter = {"teachers": 0,
                "classes": 0}
counters.delete_many({})
counters.insert_one(null_counter)

teachers.delete_many({})
classes.delete_many({})
