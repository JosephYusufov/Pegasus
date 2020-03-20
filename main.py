from backend.teacher import create_teacher, create_class

print("Would you like to wipe the database? (y/n) ")
choice = input()
if choice == "y":
    from backend import wipe_db

create_teacher("Topher Mykolyk")
create_teacher("Eric Ferencz")
create_class(0, "Software Development", 12, "https://stuycs.org")
