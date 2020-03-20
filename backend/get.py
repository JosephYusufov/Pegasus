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
    
