import sqlite3
from flask import Flask , render_template, g
import datetime
app = Flask(__name__)                                           #Her bliver der lavet en instance af Flask klassen
date = datetime.datetime.now()      


@app.route("/")        # @ er en python decorator som flask bruger tildele url.            
def index():   #Funktionen rendere forsiden og sender variabler med database med samt numerisk værdi af dags dato
    return render_template("Forside.html")        #rendere forside.html samt definere sort_data variablen til at være det samme som data. Dette gør at sort_data variablen kan bruges i html koden. samme med daysdelta


@app.route("/Oversigt")
def oversigt():#Funktionen rendere database siden og sender variabler med database med samt numerisk værdi af dags dato
    data = get_db()
    return render_template("Oversigt.html", dbdata = data, time = date)
def get_db():#Samler information fra databasen
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect('drivhus.db')
        cursor = db.cursor()
        cursor.execute("select * from data")
        all_data = cursor.fetchall()
        db.close()
    return all_data


@app.teardown_appcontext #lukker database forbindelsen
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

if __name__ == '__main__':
    app.run() #Starter flask op med login siden.
    