import sqlite3
class BatchData:
    Barcode = '' 
    Product= '' 
    EAN13 = '' 
    EAN6 = '' 
    Date = '' 
    Category = ''
    Price = 0 
    Quantity = 0 
    Batch = ''
    stockoptionbatch = False 
    stockoptionproduct = False 
    NewQuantity = 0
def data_check(): 
    BatchData.Barcode = str(BatchData.EAN13)+str(BatchData.EAN6)+str(BatchData.Batch)                                                                      #Dette er funktionen der styre hvad der sker og hvornår
    print("barcode = ", BatchData.Barcode)
    data_check_product()    
    data_check_batch()
    batch_quantity()
    if(BatchData.stockoptionproduct == True and BatchData.stockoptionbatch == False):   #Hvis vi sælger produktet men ikke har det batch bliver det bare insat i batch.db
        insert_data_batch()
    elif(BatchData.stockoptionproduct == True and BatchData.stockoptionbatch == True):  #Hvis vi sælger produktet og har det batch i databasen så opdatere vi antallet
        data_update_batch()
    batch_status_checker()
    batchdata_reset()
def data_update_batch():
    try:                                                                                #Vi har nedenstående inde i en try så programmer ikke lukker hvis der sker en fejl
        sqliteConnection = sqlite3.connect('Storedb.db')                                  #Opretter forbindelse til batch.db
        cursor = sqliteConnection.cursor()                                              #cursor er en instance af cursor() klassen hvor man kan tilslutte sqlite metoder og køre dem

        sql_update_query = """Update Stockdb set Quantity = ? where Barcode = ?""" #Vi opdatere productbatch table på antallet hvis barcode matcher
        data = (BatchData.Quantity, BatchData.Barcode)                                   #Spørgsmålstegnene ovenover betyder at vi har variabler. Her laver vi en tuple med de variabler vi gerne vil bruge
        print(data)
        cursor.execute(sql_update_query, data)                                           #Nu køre vi querien med vores tuple variabler
        sqliteConnection.commit()                                                       #Og vi skal commit for at den endelige ændring sker
        print("Batch Updated successfully")
        cursor.close()                                                                  #Derefter lukker vi cursor metoden. Hvilket for os er forbindelsen til databasen

    except sqlite3.Error as error:                                                      #Hvis der sker en fejl udprinter vi fejlbeskeden
        print("Failed to update batch table", error)
    finally:                                                                            #Til sidst kigger den på om den har en forbindelse til en database. Hvis den har det lukker den forbindelsen
        if sqliteConnection:
            sqliteConnection.close()
def insert_data_batch():
    try:                                                   #Vi har nedenstående inde i en try så programmer ikke lukker hvis der sker en fejl
        sqliteConnection = sqlite3.connect('Storedb.db')     #Opretter forbindelse til batch.db
        cursor = sqliteConnection.cursor()                 #cursor er en instance hvor man kan tilsutte sqlite metoder og køre dem
        sqlite_insert_query = """INSERT INTO Stockdb                    
                            (Barcode, Product, EAN13, EAN6, Date, Batch, Category, Price, Quantity) 
                            VALUES 
                            (?,?,?,?,?,?,?,?,?)"""                                                                                                                        #Her indsætter vi i databasen. Og vi definere kolone navnene vi gerne vil sætte ind på og derefter de værdier vi gerne vil sætte ind. Det gør vi ved ? for at vise det variabler som vi definere senere
        datatuple = (str(BatchData.Barcode), BatchData.Product, BatchData.EAN13, BatchData.EAN6, BatchData.Date, BatchData.Batch, BatchData.Category, BatchData.Price, BatchData.Quantity) #Spørgsmålstegnene ovenover betyder at vi har variabler. Her laver vi en tuple med de værdier vi gerne vil bruge
        print("row værdi: ", datatuple)
        cursor.execute(sqlite_insert_query, datatuple)                                                                                                                     #Nu køre vi querien med vores tuple variabler
        sqliteConnection.commit()                                                                                                                                       #Og vi skal commit for at den endelige ændring sker
        print("Record inserted successfully into Batch, Stockdb table ", cursor.rowcount)
        cursor.close()                                                                                                                                                  #Derefter lukker vi cursor metoden. Hvilket for os er forbindelsen til databasen

    except sqlite3.Error as error:                  #Hvis der sker en fejl udprinter vi fejlbeskeden
        print("Failed to insert data into productbatch table", error)
    finally:                                        #Til sidst kigger den på om den har en forbindelse til en database. Hvis den har det lukker den forbindelsen
        if sqliteConnection:
            sqliteConnection.close()
def batch_quantity():
    print("new quantity = ", BatchData.NewQuantity)
    print("quantity = ", BatchData.Quantity)
    if(BatchData.NewQuantity != 0):                                     #Hvis Newquantity ikke er 0 så lægger vi de antal vi allerede har sammen med det nye vi tilføjer.
        BatchData.Quantity = BatchData.Quantity + BatchData.NewQuantity
    else:                                                               #Hvis ikke s¨å trækker vi bare 1 fra det antal vi allerede har. 
        print(BatchData.Quantity)
        BatchData.Quantity = BatchData.Quantity - 1
        print(BatchData.Quantity)
        print("Ændret antal")
def batch_status_checker():
    try:                                                    #Vi har nedenstående inde i en try så programmer ikke lukker hvis der sker en fejl
        sqliteConnection = sqlite3.connect('Storedb.db')      #Opretter forbindelse til batch.db
        cursor = sqliteConnection.cursor()                  #cursor er en instance hvor man kan tilsutte sqlite metoder og køre dem

        sql_delete_query = """DELETE from Stockdb where Quantity <= ?""" #Sletter fra productbatch table hvis antallet er 0. Igen ? viser vi definere det senere
        cursor.execute(sql_delete_query, (0,))                                #Nu køre vi querien med vores tuple variabler
        sqliteConnection.commit()                                             #Og vi skal commit for at den endelige ændring sker
        print("Record deleted successfully")

        cursor.close()                                      #Derefter lukker vi cursor metoden. Hvilket for os er forbindelsen til databasen

    except sqlite3.Error as error:              #Hvis der sker en fejl udprinter vi fejlbeskeden
        print("Failed to delete reocord from a sqlite table", error)
    finally:                                    #Til sidst kigger den på om den har en forbindelse til en database. Hvis den har det lukker den forbindelsen
        if sqliteConnection:
            sqliteConnection.close()
            print("sqlite connection is closed")
def data_check_batch():
    try:                                                    #Vi har nedenstående inde i en try så programmer ikke lukker hvis der sker en fejl
        sqliteConnection = sqlite3.connect('Storedb.db')      #Opretter forbindelse til batch.db
        cursor = sqliteConnection.cursor()                  #cursor er en instance hvor man kan tilsutte sqlite metoder og køre dem

        sql_select_query = """select * from Stockdb where Barcode = ?""" #Finder alt i productbatch tablet som matcher variablen til barcode kolonnen 
        print("batch-barcode: ", BatchData.Barcode)
        print(type(BatchData.Barcode))         
        cursor.execute(sql_select_query, (BatchData.Barcode,))                  #Nu køre vi querien med vores tuple variabler
        records = cursor.fetchall()                                             #Her hiver den så alt ud af databasen og sætter records variablen lig med det
        print("Printing I ", BatchData.Barcode)
        print("records printing: ", records)
        for row in records:                                 #For loopet her køre lige så mange gange den har fået rækker ud af tabellen
            print(row)
            if(BatchData.Barcode == str(row[0])):           #Kigger på om det kolonne 1 i rækkerne matcher vores barcode variable i batchdata
                print("Vi har det batch")
                BatchData.stockoptionbatch = True           #Hvis den matcher sætter den stockoptionbatch til True for at indikere vi allerede har det batch på lager
                BatchData.Quantity = row[8]                 #Samtidig med den tager antallet der er på lager
            else:                                             
                print("row0 = ", row[0])
                print("Vi har ikke det batch")
                BatchData.stockoptionbatch = False          #Hvis den barcode ikke matcher så sætter den stockoptionbatch til False for at vise vi ikke har det batch på lager
        else:
            print("Vi har intet i databasen")
        cursor.close()                                      #Derefter lukker vi cursor metoden. Hvilket for os er forbindelsen til databasen
    except sqlite3.Error as error:                          #Hvis der sker en fejl udprinter vi fejlbeskeden
        print("Failed to read data from sqlite table", error)
    finally:                                                #Til sidst kigger den på om den har en forbindelse til en database. Hvis den har det lukker den forbindelsen
        if sqliteConnection:
            sqliteConnection.close()
def data_check_product():
    try:                                                    #Vi har nedenstående inde i en try så programmer ikke lukker hvis der sker en fejl
        sqliteConnection = sqlite3.connect('Infodb.db')     #Opretter forbindelse til batch.db
        cursor = sqliteConnection.cursor()                  #cursor er en instance hvor man kan tilsutte sqlite metoder og køre dem

        sql_select_query = """select * from Productdb where EAN13 = ?""" #Den tager alt fra product table som matcher variablen med EAN13 kolonnen
        cursor.execute(sql_select_query, (BatchData.EAN13,)) #Spørgsmålstegnene ovenover betyder at vi har variabler. Her laver vi en tuple med de variabler vi gerne vil bruge
        records = cursor.fetchall()                         #Her hiver den så alt ud af databasen og sætter records variablen lig med det
        print("Printing ID ", BatchData.EAN13)
        for row in records:                                 #For loopet her køre lige så mange gange den har fået rækker ud af tabellen       
            print(row[0])
            print("EAN13: ", BatchData.EAN13)
            if(BatchData.EAN13 == row[0]):                  #Kigger på om der er nogle rækker med deres kolonne 1 matcher EAN13 i batchdata
                print("Vi har produktet")
                BatchData.stockoptionproduct = True         #Hvis den matcher sætter den stockoptionproduct variablen til True for at vise vi sælger produktet
                BatchData.Product = row[1]                  #Defefter sætter den product variablen til kolonne 2 som er produkt navnet
                BatchData.Category = row[2]                 #Her sætter den Category variablen til kolonne 3 som er kategorien varen tilhøre
                BatchData.Price = row[3]                    #Her sætter den price variablen til kolonne 4 som er prisen på varen
            else:   
                BatchData.stockoptionproduct = False        #Hvis den ikke matcher sætter den stockoption product til False for at vise det er et produkt vi ikke sælger
                print("Vi har ikke produktet")
        cursor.close()                                      #Derefter lukker vi cursor metoden. Hvilket for os er forbindelsen til databasen
    except sqlite3.Error as error:                          #Hvis der sker en fejl udprinter vi fejlbeskeden
        print("Failed to read data from sqlite table", error)
    finally:                                                #Til sidst kigger den på om den har en forbindelse til en database. Hvis den har det lukker den forbindelsen
        if sqliteConnection:
            sqliteConnection.close()
def batchdata_reset():                                                  #Denne funktion resetter alle variabler i batchdata klassen så vi er klar til en ny vare og ikke har gammel information hængene
    BatchData.Barcode = '' 
    BatchData.Product= '' 
    BatchData.EAN13 = ''
    BatchData.EAN6 = '' 
    BatchData.Date = '' 
    BatchData.Category = ''
    BatchData.Price = 0 
    BatchData.Quantity = 0
    BatchData.stockoptionbatch = False 
    BatchData.stockoptionproduct = False
    BatchData.NewQuantity = 0
    print("Batchdata is now reset")
def insert_data_products():                                                                                 #Denne funktion bliver brugt til at tilføje vare ind i produkt databasen. Hvilket er den database der viser hvilke vare vi sælger, kategorien og prisen på varen. Denne viser ikke om vi har det på lager
    try:                                                                                                    #Vi har nedenstående inde i en try så programmer ikke lukker hvis der sker en fejl
        sqliteConnection = sqlite3.connect('product.db')                                                    #Opretter forbindelse til product.db
        cursor = sqliteConnection.cursor()                                                                  #cursor er en instance hvor man kan tilsutte sqlite metoder og køre dem
        sqlite_insert_query = """INSERT INTO Products
                            (EAN13, Product,Category, Price) 
                            VALUES 
                            (7392701574172, 'Faxe kondi 0,5L', 'Drikkevare', 20)"""
                                                                                                            #Ovenover sætter vi et produkt ind i product tabellen. Denne gang uden ? og har derfor skrevet værdierne direkte ind
        cursor.execute(sqlite_insert_query)                                                                  #Nu køre vi querien
        sqliteConnection.commit()                                                                           #Her comitter vi
        print("Record inserted successfully into SqliteDb_developers table ", cursor.rowcount)
        cursor.close()                                                                                      #Derefter lukker vi cursor metoden. Hvilket for os er forbindelsen til databasen
    except sqlite3.Error as error:                                                                          #Hvis der sker en fejl udprinter vi fejlbeskeden
        print("Failed to read data from sqlite table", error)
    finally:                                                                                                #Til sidst kigger den på om den har en forbindelse til en database. Hvis den har det lukker den forbindelsen
        if sqliteConnection:
            sqliteConnection.close()

def batch_delete():
    try:                                                    #Vi har nedenstående inde i en try så programmer ikke lukker hvis der sker en fejl
        sqliteConnection = sqlite3.connect('Storedb.db')      #Opretter forbindelse til batch.db
        cursor = sqliteConnection.cursor()                  #cursor er en instance hvor man kan tilsutte sqlite metoder og køre dem

        sql_delete_query = """DELETE from Stockdb where Quantity > ?""" #Sletter fra productbatch table hvis antallet er 0. Igen ? viser vi definere det senere
        cursor.execute(sql_delete_query, (0,))                                #Nu køre vi querien med vores tuple variabler
        sqliteConnection.commit()                                             #Og vi skal commit for at den endelige ændring sker
        print("Record deleted successfully")

        cursor.close()                                      #Derefter lukker vi cursor metoden. Hvilket for os er forbindelsen til databasen

    except sqlite3.Error as error:              #Hvis der sker en fejl udprinter vi fejlbeskeden
        print("Failed to delete reocord from a sqlite table", error)
    finally:                                    #Til sidst kigger den på om den har en forbindelse til en database. Hvis den har det lukker den forbindelsen
        if sqliteConnection:
            sqliteConnection.close()
            print("sqlite connection is closed")
def insert_data_returndb():
    try:                                                   #Vi har nedenstående inde i en try så programmer ikke lukker hvis der sker en fejl
        sqliteConnection = sqlite3.connect('Infodb.db')     #Opretter forbindelse til batch.db
        cursor = sqliteConnection.cursor()                 #cursor er en instance hvor man kan tilsutte sqlite metoder og køre dem
        sqlite_insert_query = """INSERT INTO Returnbatchdb                    
                            (Batch) 
                            VALUES 
                            (?)"""                                                                                                                        #Her indsætter vi i databasen. Og vi definere kolone navnene vi gerne vil sætte ind på og derefter de værdier vi gerne vil sætte ind. Det gør vi ved ? for at vise det variabler som vi definere senere
        datatuple = ("9615348218911008200ABCD1234",) 
        print("row værdi: ", datatuple)
        cursor.execute(sqlite_insert_query, datatuple)                                                                                                                     #Nu køre vi querien med vores tuple variabler
        sqliteConnection.commit()                                                                                                                                       #Og vi skal commit for at den endelige ændring sker
        print("Record inserted successfully into Batch, Stockdb table ", cursor.rowcount)
        cursor.close()                                                                                                                                                  #Derefter lukker vi cursor metoden. Hvilket for os er forbindelsen til databasen

    except sqlite3.Error as error:                  #Hvis der sker en fejl udprinter vi fejlbeskeden
        print("Failed to insert data into productbatch table", error)
    finally:                                        #Til sidst kigger den på om den har en forbindelse til en database. Hvis den har det lukker den forbindelsen
        if sqliteConnection:
            sqliteConnection.close()

#batch_delete()
#insert_data_returndb()