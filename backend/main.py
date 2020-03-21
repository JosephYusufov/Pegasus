from backend.teacher import create_teacher, create_class
from backend.get import get_teacher, get_class, get_counters, get_all_teachers, get_all_classes
from pprint import pprint

# print("Would you like to wipe the database? (y/n) ")
# choice = input()
# if choice == "y":
from backend import wipe_db

create_teacher("Topher Mykolyk")
create_class(0, "Software Development", 12, "https://stuycs.org")
create_teacher("Eric Ferencz")
create_class(1, "Womens Voices", 13, "https://mrferencz.blogspot.com")

# get_teacher(0)
# get_class(0)
# get_counters()
# pprint(get_all_teachers())
