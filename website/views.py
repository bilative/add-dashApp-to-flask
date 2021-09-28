import pymongo
import json
from flask import Blueprint, render_template
import pandas as pd

client = pymongo.MongoClient('mongodb://username:password@ip:port/')

views = Blueprint("views", __name__)

db = client["website"]
schema = db["posts"]

@views.route("/")
@views.route("/home")
def home():
    return render_template("home.html")



@views.route("/writings/x-days-of-code")
def xdaysofcode():
    df = pd.DataFrame(schema.find({}))
    posts = df['post'].apply(lambda x: x.replace("\n", " ").replace("  ", ""))

    return render_template("x-days-of-code.html", posts=posts[::-1])