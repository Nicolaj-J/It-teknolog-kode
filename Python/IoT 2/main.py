import dbHandler
import EAN5conversion
import sqlite3
def start(barcode):
    if(str(barcode) == str(000000000000000000)):
        dbHandler.BatchData.QuantityHandling = True
        print(dbHandler.BatchData.QuantityHandling)
    elif(str(barcode) == str(111111111111111111)):
        dbHandler.BatchData.QuantityHandling = False
        print(dbHandler.BatchData.QuantityHandling)
    else:
        if(dbHandler.BatchData.QuantityHandling == False):
            EAN13 = str(barcode)[0:13]
            EAN5 = str(barcode)[13:18]
            dbHandler.BatchData.Barcode = barcode #fundet
            dbHandler.BatchData.EAN13 = int(EAN13) #fundet
            dbHandler.BatchData.EAN5 = int(EAN5) #fundet
            dbHandler.BatchData.Date = EAN5conversion.dato_konvertering(int(EAN5))    #dbHandler.data_check()
            dbHandler.data_check()
def deleteRecord():
    try:
        sqliteConnection = sqlite3.connect('batch.db')
        cursor = sqliteConnection.cursor()

        sql_update_query = """DELETE from Productbatch where Product = ?"""
        cursor.execute(sql_update_query, ('Sødmælk',))
        sqliteConnection.commit()
        print("Record deleted successfully")

        cursor.close()

    except sqlite3.Error as error:
        print("Failed to delete reocord from a sqlite table", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print("sqlite connection is closed")

x = input()
if(x == "delete"):
    deleteRecord()
elif(x == "start"):
    start(123456789123400067)

#000000000000000000  start indscanning
#111111111111111111  stop indscanning
#123456789123456789  stregkode med ean13 og ean5