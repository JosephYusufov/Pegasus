from pymongo import MongoClient
from pprint import pprint
from bson.json_util import loads
import json
import datetime


client = MongoClient()
db = client.pegasus
teachers = db.teachers
classes = db.classes
counters = db.counters

def get_teacher(teacher_ID):
    this_teacher_query = {"ID": teacher_ID} # query to find the teacher 
    this_teacher = db.teachers.find_one(this_teacher_query)
    full_classes = []
    for member in this_teacher["classes"]:
        full_classes.append(db.classes.find_one({"ID": member}))
    this_teacher["classes"] = full_classes
    # pprint(this_teacher)
    return this_teacher

def get_all_teachers():
    to_return = []
    for member in teachers.find():
        to_return.append(get_teacher(member['ID']))
    return to_return
        
def get_class(class_ID):
    this_class_query = {"ID": class_ID} # query to find the class
    this_class = db.classes.find_one(this_class_query)
    # pprint(this_class)
    return this_class

def get_all_classes():
    to_return = []
    for member in classes.find():
        to_return.append(member)
    return to_return

def get_counters():
    counters = db.counters.find_one({})
    # pprint(counters)
    return counters
