import sqlite3
from flask import Flask, redirect, url_for, render_template, request, session, g
import datetime
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager , UserMixin , login_required ,login_user, logout_user,current_user ,login_url,set_login_view

#Udregner dato og 10 dage frem
date1 = datetime.datetime.now() + datetime.timedelta(days=10)   
date = datetime.datetime.now()
date2 = datetime.datetime(day=1, month=1, year=2000)
timedelta10 = date1 - date2
timedelta = date - date2
print(timedelta)

app = Flask(__name__) #Laver en instance af flask

#Sætter op flask login
app.secret_key = "r@nd0mSk_1"
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///db.db'
app.config['SECRET_KEY']='619619'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=True
db = SQLAlchemy(app)

#Starter Flask login
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "/"

#Laver en class til database håndtering
class User(UserMixin,db.Model):
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    username = db.Column(db.String(200))
    email = db.Column(db.String(200))
    password = db.Column(db.String(200))

#Indeholder login informationer
@login_manager.user_loader
def get(id):
    return User.query.get(id)

# login funktionerne
@app.route('/',methods=['GET'])
def get_login():                               
    return render_template('Login.html')
@app.route('/',methods=['POST'])
def login_post():
    email = request.form['email']       #Trækker information ud af login felter
    password = request.form['password'] #Trækker information ud af login felter
    user = User.query.filter_by(email=email).first() #Scanner igennem DB for brugere
    userpassword = User.query.filter_by(password=password).first() #Scanner igennem DB for brugere
    print(user)
    print("password ", userpassword)
    if user != None and user == userpassword: #Hvis den finder et match i databasen kan du logge ind
        login_user(user) #Laver en session til din bruger
        return redirect('/forside')
    else: 
        return render_template('Login.html')

#log ud funktionen
@app.route('/logout',methods=['GET'])
def logout():                     
    logout_user() #Logger ud af session
    return redirect('/')

#Forside funktionenerne 
@app.route('/forside', methods =["GET", "POST"])
@login_required #Kræver du har en aktiv session for at bruge denne side. 
def forside(): 
    data = get_dbforside()
    batch = batchsplit(get_db_batch())
    if request.method == "POST": #her trækkes der information ud af hjemmesiden når man vil rætte prisen
        barcode = request.form.get("barcode")
        pris = request.form.get("price")
        update_database(barcode, pris)
        print(pris, " ", barcode)
        data = get_dbforside()
        batch = batchsplit(get_db_batch())
        return render_template("Forside.html", sort_data = data, var = timedelta.days, batch = batch )
    return render_template('Forside.html',  sort_data = data, var = timedelta.days, batch = batch)
def get_dbforside(): #Samler information fra databasen
    try:                                                   
        sqliteConnection = sqlite3.connect('Storedb.db')
        cursor = sqliteConnection.cursor()       
        cursor.execute("select * from Stockdb")
        sort_data = cursor.fetchall()
        cursor.close()                                                                                                                                                 
    except sqlite3.Error as error:
        print("Failed to select data from Infodb.db Returnbatchdb table", error)
    finally: 
        if sqliteConnection:
            sqliteConnection.close()                                                              
    return sort_data     
                                              
#Tilbagekalds siden funktionerne
@app.route("/Tilbagekald")        
@login_required     #Kræver du har en aktiv session for at bruge denne side.        
def tilbagekald():   
    batch = batchsplit(get_db_batch())
    return render_template("Batch.html", batch = batch)        
def get_db_batch():
    try:                                                   
        sqliteConnection = sqlite3.connect('Infodb.db')
        cursor = sqliteConnection.cursor()       
        cursor.execute("select * from Returnbatchdb")
        batchdata = cursor.fetchall()
        cursor.close()                                                                                                                                                 
        print("batchdata = ", batchdata)
    except sqlite3.Error as error:
        print("Failed to select data from Infodb.db Returnbatchdb table", error)
    finally: 
        if sqliteConnection:
            sqliteConnection.close()
    return batchdata 
def batchsplit(batch):
    tilbagekaldslist = []
    print("len: ", len(batch))
    print("batch: ", batch[0])
    print("batch i 1: ", batch[0][1])
    print("count: ", batch.count('('))
    for i in range (0, len(batch) +1):
        print(i)
        try:                                                   
            sqliteConnection = sqlite3.connect('Storedb.db')
            cursor = sqliteConnection.cursor()
            cursor.execute("select * from Stockdb where barcode = ?", (str(batch[i -1][1]),))
            batchall = cursor.fetchall()
            print("batchall: ",batchall)
            if len(batchall) != 0:
                batchall = batchall[0]
                batchall = batchall +  (batch[i -1][2],)
                tilbagekaldslist.append(batchall)
                cursor.close()                                                                                                                                                 
        except sqlite3.Error as error:
            print("Failed to select data from Infodb.db Returnbatchdb table", error)
        finally: 
            if sqliteConnection:
                sqliteConnection.close()
    print(tilbagekaldslist)
    return tilbagekaldslist

#Ansatte siden funktionerne
@app.route("/Ansatte")        # @ er en python decorator som flask bruger tildele url.
@login_required     #Kræver du har en aktiv session for at bruge denne side.        
def ansatte():   
    ansatte = None
    return render_template("Ansatte.html", ansatte = ansatte) 

#Database side funktionerne
@app.route("/db",methods=['GET','POST'])
@login_required#Kræver du har en aktiv session for at bruge denne side. 
def database(): #Funktionen rendere database siden og sender variabler med database med samt numerisk værdi af dags dato
    data = get_db_stock()
    batch = get_db_batch()
    if request.method == "POST":
       barcode = request.form.get("barcode")
       pris = request.form.get("price")
       update_database(barcode, pris)
       print(pris, " ", barcode)
       data = get_dbforside()
       batch = batchsplit(get_db_batch())
       return render_template("Database.html", all_data = data, var = timedelta.days, batchdata = batch )
    print(data)
    return render_template("Database.html", all_data = data, var = timedelta.days, batchdata = batch )
def get_db_stock():#Samler information fra databasen
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect('Storedb.db')
        cursor = db.cursor()
        cursor.execute("select * from Stockdb")
        all_data = cursor.fetchall()
        db.close()
    return all_data

#Funktionen til at rette pris
def update_database(barcode, price):
    try:                                                                                #Vi har nedenstående inde i en try så programmer ikke lukker hvis der sker en fejl
        sqliteConnection = sqlite3.connect('Storedb.db')                                #Opretter forbindelse til batch.db
        cursor = sqliteConnection.cursor()                                              #cursor er en instance af cursor() klassen hvor man kan tilslutte sqlite metoder og køre dem

        sql_update_query = """Update Stockdb set Price = ? where Barcode = ?"""         #Vi opdatere productbatch table på antallet hvis barcode matcher
        data = (price, barcode)                                                         #Spørgsmålstegnene ovenover betyder at vi har variabler. Her laver vi en tuple med de variabler vi gerne vil bruge
        print(data)
        cursor.execute(sql_update_query, data)                                          #Nu køre vi querien med vores tuple variabler
        sqliteConnection.commit()                                                       #Og vi skal commit for at den endelige ændring sker
        print("Batch Updated successfully")
        cursor.close()                                                                  #Derefter lukker vi cursor metoden. Hvilket for os er forbindelsen til databasen

    except sqlite3.Error as error:                                                      #Hvis der sker en fejl udprinter vi fejlbeskeden
        print("Failed to update batch table", error)
    finally:                                                                            #Til sidst kigger den på om den har en forbindelse til en database. Hvis den har det lukker den forbindelsen
        if sqliteConnection:
            sqliteConnection.close()

@app.teardown_appcontext #lukker database forbindelsen
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

if __name__ == '__main__':
    app.run(host="0.0.0.0") #Starter flask op med login siden.
    