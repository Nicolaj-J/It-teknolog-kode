import sqlite3
from flask import Flask, session, render_template, request, g
import datetime
app = Flask(__name__)
app.secret_key = "select_a_COMPLEX_secret_key_please"
date1 = datetime.datetime.now() + datetime.timedelta(days=10)
date = datetime.datetime.now()
date2 = datetime.datetime(day=1, month=1, year=2000)
timedelta10 = date1 - date2
timedelta = date - date2


@app.route("/main")
def forside():
    data = get_dbforside()
    print(data)
    return render_template("Forside.html", sort_data = data, var = timedelta.days)
def get_dbforside():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect('batch.db')
        cursor = db.cursor()
        sql_select_query = """select * from productbatch where EAN5 < ? order by EAN5 asc"""
        cursor.execute(sql_select_query, (timedelta10.days,))
        sort_data = cursor.fetchall()
        db.close()
    return sort_data

@app.route("/db")
def database():
    data = get_db()
    print(data)
    return render_template("Database.html", all_data = data, var = timedelta.days )
def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect('batch.db')
        cursor = db.cursor()
        cursor.execute("select * from productbatch")
        all_data = cursor.fetchall()
        db.close()
    return all_data


@app.route("/")
def index():
    return render_template("Login.html")


@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

if __name__ == '__main__':
    app.run()
    