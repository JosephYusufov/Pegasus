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


def create_teacher(name):
    teacher_ID = counters.find_one().get("teachers") # Get most recent teacher ID
    increment_counter = { "$set": {"teachers": teacher_ID + 1 }} # command to increment counter
    counters.update_many({}, increment_counter) # incrementing the counter
    new_teacher = {"name": name,
                   "ID": teacher_ID,
                   "classes": []}
    new_teacher = teachers.insert_one(new_teacher) # inserting the new teacher into collection
    return new_teacher # return _id of new teacher document in the collection
    
    
def create_class(teacher_ID, class_name, class_time, class_link):
    class_ID = counters.find_one().get("classes") # get most recent class ID
    increment_counter = { "$set": {"classes": class_ID + 1 }} # command to increment counter
    counters.update_many({}, increment_counter) # incrementing the counter

    new_class = {"name": class_name,
                 "time": class_time,
                 "link": class_link,
                 "ID"  : class_ID,
                 "teacher_ID": teacher_ID}    
    new_class = classes.insert_one(new_class) # inserting new class into collection


    # SUPER ANNOYING BUG HERE :: 2020-03-19 02:25
    this_teacher_query = {"ID": str(teacher_ID)} # query to find the teacher of this class
    this_teacher = db.teachers.find_one(this_teacher_query)
    print("teacher")
    pprint(this_teacher)
    
    # this_teacher_classes = this_teacher.classes # variable to store this teachers list of classes
    # this_teacher_classes.append(class_ID) # adding this class ID to this teacher's document
    # class_to_append = {"$set": {"classes": this_teacher_classes}} # command to update this teachers class list
    # teachers.update_one(this_teacher_query, class_to_append) # updating the teachers class list.
    
    return new_class 

