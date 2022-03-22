from pickle import TRUE
import sqlite3
class data:
    username = '' 
    password = ''
    usernamedb = ''
    passworddb = ''
def readSqliteTable():
    try:
        sqliteConnection = sqlite3.connect('Login.db')
        cursor = sqliteConnection.cursor()
        print("Connected to SQLite")

        sql_select_query = """select * from Login where username = ?"""
        cursor.execute(sql_select_query, (data.username,))
        records = cursor.fetchall()
        print("Total rows are:  ", len(records))
        print("Printing each row")
        for row in records:
            data.usernamedb = row[0]
            data.passworddb = row[1]
           

        cursor.close()

    except sqlite3.Error as error:
        print("Failed to read data from sqlite table", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print("The SQLite connection is closed")
 
def insertVaribleIntoTable():
    try:
        sqliteConnection = sqlite3.connect('Login.db')
        cursor = sqliteConnection.cursor()
        print("Connected to SQLite")

        sqlite_insert_with_param = """INSERT INTO Login
                          (username,password )
                          VALUES
                          (?, ?);"""

        data_tuple = (data.username,data.password)
        cursor.execute(sqlite_insert_with_param, data_tuple)
        sqliteConnection.commit()
        print("Python Variables inserted successfully into SqliteDb_developers table")

        cursor.close()

    except sqlite3.Error as error:
        print("Failed to insert Python variable into sqlite table", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print("The SQLite connection is closed")

x = input()
if(x == 'reg'):
    print("Username: ")
    data.username = input()
    print("password: ")
    data.password = input()
    insertVaribleIntoTable()
if(x == 'login'):
    print("Username: ")
    data.username = input()
    print("password: ")
    data.password = input()
    readSqliteTable()
    print("usernamedb: ", data.usernamedb)
    print("passworddb: ", data.passworddb)
    print("Username: ", data.username)
    print("password: ", data.password)
    if(data.username and data.password == data.usernamedb and data.passworddb):
        print("Login successful")
    else: 
        print("Login failed")

