from flask import Flask, render_template, request
from backend.get import get_teacher, get_class, get_counters, get_all_classes, get_all_teachers
from backend import main
from pprint import pprint
import os

app = Flask(__name__)
app.secret_key = os.urandom(32)

@app.route("/")
def welcome():
    if request.args:
        
        return render_template("index.html", data=data)
    teachers = get_all_teachers()
    pprint(teachers)
    return render_template("index.html", teachers=teachers)

if __name__ == "__main__":
    app.debug = True
    app.run(host='0.0.0.0')
