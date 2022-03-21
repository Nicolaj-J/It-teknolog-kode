from flask import Flask, make_response
from flask import render_template,redirect
import datetime
import sqlite3
import json
date = datetime.datetime.now() + datetime.timedelta(days=10)
app = Flask(__name__)
år = str(date)[0:4]
måned = str(date)[5:7]
dage = str(date)[8:10]
dato = f"{dage}/{måned}/{år}"
print(dato)

def getDBData():
    try:
        sqliteConnection = sqlite3.connect('batch.db')
        cursor = sqliteConnection.cursor()

        sql_select_query = """select * from productbatch where Date < ?"""
        cursor.execute(sql_select_query, (dato,))
        records = cursor.fetchall()
        cursor.close()
        return records
    except sqlite3.Error as error:
        print("Failed to read data from sqlite table", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
@app.route('/')
def login():
    return (render_template("Forside_login.html"))


@app.route('/db')
def db():
    return (render_template("Database.html"))

@app.route('/data', methods=["POST"])
def data():
    conn = sqlite3.connect('batch.db')
    posts = conn.execute('SELECT * FROM productbatch').fetchall()
    conn.close()
    return render_template('Database.html', posts=posts)


    #print(getDBData())
    #print(len(getDBData()))
    #response = make_response(json.dumps(data))
    #response.content_type = "application/json"
    #return response
if __name__ == "main":
    app.run(threaded=True)

