import sqlite3
import random
from flask import Flask, session, render_template, request, g
import datetime
app = Flask(__name__)
app.secret_key = "select_a_COMPLEX_secret_key_please"
date = datetime.datetime.now() + datetime.timedelta(days=10)
app = Flask(__name__)
år = str(date)[0:4]
måned = str(date)[5:7]
dage = str(date)[8:10]
dato = f"{dage}/{måned}/{år}"

@app.route("/db")
def database():
    data = get_db()
    print(data)
    return render_template("Database.html", all_data = data)
def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect('batch.db')
        cursor = db.cursor()
        cursor.execute("select * from productbatch")
        all_data = cursor.fetchall()

    return all_data

@app.route("/")
def index():
    data = get_dbforside()
    print(data)
    return render_template("forside.html", sort_data = data)
def get_dbforside():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect('batch.db')
        cursor = db.cursor()
        sql_select_query = """select * from productbatch where Date > ? order by EAN5 asc"""
        cursor.execute(sql_select_query, (dato,))
        sort_data = cursor.fetchall()

    return sort_data



@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

if __name__ == '__main__':
    app.run()
    