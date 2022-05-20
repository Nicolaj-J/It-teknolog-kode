import dbHandler
import EAN5conversion
import sqlite3
Barcodedic = {

}
def barcode_Split(barcode):
    val1 = -1
    val2 = -1
    barcode = barcode + '-'
    print(barcode)
    for i in range(1, barcode.count(')')+1):
        val1 = barcode.find('(', val1 + 1)
        val2 = barcode.find(')', val2 + 1)
        if(i == barcode.count('(')):
            Barcodedic[barcode[val1 +1:val2]] = barcode[val2 +1:barcode.find('(', val1 + 3)]
        elif(i < barcode.count('(')):
            Barcodedic[barcode[val1 +1:val2]] = barcode[val2 +1:barcode.find('(', val1 + 2)]
    print(Barcodedic)
        





barcode_Split('(01)03453120000011(17)120508(10)ABCD1234(410)9501101020917')

def start(barcode):                                                             #Denne funktion bliver kaldt med en stregkode(argument)                                                 
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
        sqliteConnection = sqlite3.connect('infodb.db')
        cursor = sqliteConnection.cursor()

        sql_update_query = """DELETE from Identifiersdb where Data = ?"""
        cursor.execute(sql_update_query, ("Serial Shipping Container Code",))
        sqliteConnection.commit()
        print("Record deleted successfully")

        cursor.close()

    except sqlite3.Error as error:
        print("Failed to delete reocord from a sqlite table", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print("sqlite connection is closed")
'''
def insert():
    try:                                                   #Vi har nedenstående inde i en try så programmer ikke lukker hvis der sker en fejl
        sqliteConnection = sqlite3.connect('')     #Opretter forbindelse til batch.db
        cursor = sqliteConnection.cursor()                 #cursor er en instance hvor man kan tilsutte sqlite metoder og køre dem
    

        sqlite_insert_query = """INSERT INTO Identifiersdb                    
                            (Identifier, Data) 
                            VALUES 
                         (?,?)"""                                                                                                                        #Her indsætter vi i databasen. Og vi definere kolone navnene vi gerne vil sætte ind på og derefter de værdier vi gerne vil sætte ind. Det gør vi ved ? for at vise det variabler som vi definere senere
        tuple1 = ("99", "Interne applikationer")
        print("row værdi: ", tuple1)
        cursor.execute(sqlite_insert_query, tuple1)                                                                                                                     #Nu køre vi querien med vores tuple variabler
        sqliteConnection.commit()                                                                                                                                       #Og vi skal commit for at den endelige ændring sker
        print("Record inserted successfully into Batch, Productbatch table ", cursor.rowcount)
        cursor.close()                                                                                                                                                  #Derefter lukker vi cursor metoden. Hvilket for os er forbindelsen til databasen

    except sqlite3.Error as error:                  #Hvis der sker en fejl udprinter vi fejlbeskeden
        print("Failed to insert data into productbatch table", error)
    finally:                                        #Til sidst kigger den på om den har en forbindelse til en database. Hvis den har det lukker den forbindelsen
        if sqliteConnection:
            sqliteConnection.close()'''
#insert()
#delete()
#start('0096153482189110815212')
#start('0096153482189110812550')
#start('00961534821891110820')


