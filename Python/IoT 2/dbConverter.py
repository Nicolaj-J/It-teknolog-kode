import dbHandler
import EAN5conversion
import sqlite3
def start(barcode):                                                             #Denne funktion bliver kaldt med en stregkode
                                                     
    if(len(str(barcode)[2:22])==20):                                            #Ser på om stregkoden er 20 cifre
        print("Tilføjer") #indscanning
        EAN13 = str(barcode)[2:15]                                              #Finder EAN13 stregkoden i de 18 cifre
        EAN5 = str(barcode)[15:20]                                              #Finder EAN5 stregkoden i de 18 cifre
        Quantity = str(barcode)[20:22]                                          #Finder antallet af vare der skal tilføjes
        dbHandler.BatchData.NewQuantity = int(Quantity)                         #Sætter variablen newquantity i batchdata til antallet af vare
        dbHandler.BatchData.Barcode = str(barcode)[2:20]                        #Sætter variablen barcode i batchdata til den fulde længde af stregkoden
        dbHandler.BatchData.EAN13 = str(EAN13)                                  #Sætter variablen EAN13 i batchdata til EAN13
        dbHandler.BatchData.EAN5 = str(EAN5)                                    #Sætter variablen EAN5 i batchdata til EAN5
        dbHandler.BatchData.Date = EAN5conversion.dato_konvertering(int(EAN5))  #Kalder dato_konverterings funktionen med EAN5 stregkoden
        dbHandler.data_check()                                                  #Kalder data_check funktionen
    elif(len(str(barcode[2:20]))== 18):                                         #Ser på om stregkoden er 18 cifre
        print("fjerner") #udscanning
        EAN13 = str(barcode)[2:15]                                              #Finder EAN13 stregkoden i de 18 cifre
        EAN5 = str(barcode)[15:20]                                              #Finder EAN5 stregkoden i de 18 cifre
        dbHandler.BatchData.Barcode = str(barcode)[2:20]                        #Sætter variablen barcode i batchdata til den fulde længde af stregkoden
        dbHandler.BatchData.EAN13 = str(EAN13)                                  #Sætter variablen EAN13 i batchdata til EAN13
        dbHandler.BatchData.EAN5 = str(EAN5)                                    #Sætter variablen EAN5 i batchdata til EAN5
        dbHandler.BatchData.Date = EAN5conversion.dato_konvertering(int(EAN5))  #Kalder dato_konverterings funktionen med EAN5 stregkoden
        dbHandler.data_check()                                                  #Kalder data_check funktionen
def delete():                               #denne funktion bliver kun brugt til fejlrettelser og test
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
#start('0096153482189110732070')
#start('0096153482189110812550')
#start('00961534821891110820')


