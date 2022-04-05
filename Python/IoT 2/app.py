import sqlite3
from flask import Flask , render_template, g
import datetime
app = Flask(__name__)                                           #Her bliver der lavet en instance af Flask klassen
date1 = datetime.datetime.now() + datetime.timedelta(days=10)   #Bruger datetime modulet til at få dags dato og ligge 10 dage oven i
date = datetime.datetime.now()      
date2 = datetime.datetime(day=1, month=1, year=2000)
timedelta10 = date1 - date2
timedelta = date - date2


@app.route("/main")        # @ er en python decorator som flask bruger tildele url.            
def forside():   #Funktionen rendere forsiden og sender variabler med database med samt numerisk værdi af dags dato
    data = get_dbforside()
    print(data)
    return render_template("Forside.html", sort_data = data, daysdelta = timedelta.days)        #rendere forside.html samt definere sort_data variablen til at være det samme som data. Dette gør at sort_data variablen kan bruges i html koden. samme med daysdelta
def get_dbforside(): #Samler information fra databasen
    db = getattr(g, '_database', None)          #klargøre til at lave database intruksen
    if db is None:                              #Kigger på om der er en database forbindelse
        db = g._database = sqlite3.connect('batch.db') #laver instruksen færdig til oprettelse af forbindelse 
        cursor = db.cursor()                            #laver en instance af cursor til oprettelse af forbindelse
        sql_select_query = """select * from productbatch where EAN5 < ? order by EAN5 asc"""    #definere vores query
        cursor.execute(sql_select_query, (timedelta10.days,))           #opretter forbindelse og Køre queryen
        sort_data = cursor.fetchall()                                   #Trækker resultatet ud af databasen
        db.close()                                                      #Lukker forbindelsen
    return sort_data                                                    #Returnere dataen

@app.route("/db")
def database():#Funktionen rendere database siden og sender variabler med database med samt numerisk værdi af dags dato
    data = get_db()
    print(data)
    return render_template("Database.html", all_data = data, var = timedelta.days )
def get_db():#Samler information fra databasen
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect('batch.db')
        cursor = db.cursor()
        cursor.execute("select * from productbatch")
        all_data = cursor.fetchall()
        db.close()
    return all_data


@app.route("/")
def index(): #Funktionen rendere login siden
    return render_template("Login.html")


@app.teardown_appcontext #lukker database forbindelsen
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

if __name__ == '__main__':
    app.run() #Starter flask op med login siden.
    