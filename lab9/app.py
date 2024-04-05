import sqlite3
import random
from flask import Flask, session, render_template, request, g
from model.poem import Poem

app = Flask(__name__)
# app.secret_key = "manbearpig MUDMAN888"


@app.route("/")
def index():
    db = get_db()
    data = get_poems(db)
    poems = []
    for row in data:
        poems.append(Poem(row[1], row[2], row[3]))
    return render_template("index_model.html", all_data=poems)
    # return render_template("index.html", all_data=data)


# @app.route("/add_items", methods= ["post"])
# def add_items ():
#     return request.form ["select items"]


def get_db():
    # is there any previous connection to the database?
    # to prevent connecting more than once.
    # Imagine if we have 1000 requests, we don't want to have 1000 connection
    db = getattr(g, "_database", None)
    if db is None:
        # if not, then create new connection
        db = g._database = sqlite3.connect("poem.db")
    return db

def get_poems(db):
    cursor = db.cursor()
    cursor.execute("select * from poems")
    all_data = cursor.fetchall()
    return all_data

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, "_database", None)
    if db is not None:
        db.close()


if __name__ == "__main__":
    app.run(debug=True)
