import dbHandler
import EAN5conversion
import sqlite3
def start(barcode):
    if(len(str(barcode[2:20]))== 18):
        print("fjerner")
        EAN13 = str(barcode)[2:15]
        EAN5 = str(barcode)[15:20]
        dbHandler.BatchData.Barcode = str(barcode)[2:20] 
        dbHandler.BatchData.EAN13 = str(EAN13) 
        dbHandler.BatchData.EAN5 = str(EAN5) 
        dbHandler.BatchData.Date = EAN5conversion.dato_konvertering(int(EAN5))    
        dbHandler.data_check()
    if(len(str(barcode)[2:22])==20):
        print("Tilføjer")
        EAN13 = str(barcode)[2:15]
        EAN5 = str(barcode)[15:20]
        Quantity = str(barcode)[20:22]
        dbHandler.BatchData.NewQuantity = int(Quantity)
        dbHandler.BatchData.Barcode = str(barcode)[2:20] 
        dbHandler.BatchData.EAN13 = str(EAN13) 
        dbHandler.BatchData.EAN5 = str(EAN5) 
        dbHandler.BatchData.Date = EAN5conversion.dato_konvertering(int(EAN5))
        dbHandler.data_check()
def delete():
    try:
        sqliteConnection = sqlite3.connect('batch.db')
        cursor = sqliteConnection.cursor()

        sql_update_query = """DELETE from Productbatch where Category = ?"""
        cursor.execute(sql_update_query, ('Mejeri',))
        sqliteConnection.commit()
        print("Record deleted successfully")

        cursor.close()

    except sqlite3.Error as error:
        print("Failed to delete reocord from a sqlite table", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print("sqlite connection is closed")
#delete()
start('00961534821891108120')
start('0096153482189110812550')
start('00961534821891110820')