import sqlite3
import sys
conn=sqlite3.connect('batchdatabase.db')
curs=conn.curser()

def update_data(barcode):
    pass

def add_new_data(barcode, Product, ean13 ,ean5, date, category,price, quantity):
    curs.execute("INSERT INTO DHT_data values(datetime('now'), (?), (?))", (barcode, Product, ean13 ,ean5, date, category,price, quantity))    
    conn.commit()


add_new_data (131034769125108108, "Arla Øko Sødmælk", 1310347691251 ,8108, "14/2/2022", "Mejeri","12", 1)
print ("\nEntire database contents:\n")
for row in curs.execute("SELECT * FROM DHT_data"):
    print (row)
# close the database after use
conn.close()