class variables:
    størelse = ""
    køn = ""
    vare = ""
    antal = 0
    nytantal = 0
#funktion til håndtering af filen
    #kør sql select funtkion. Find vare og træk antal ud
    def data_check_batch():
        try:                                                    #Vi har nedenstående inde i en try så programmer ikke lukker hvis der sker en fejl
            sqliteConnection = sqlite3.connect('Storedb.db')      #Opretter forbindelse til batch.db
            cursor = sqliteConnection.cursor()                  #cursor er en instance hvor man kan tilsutte sqlite metoder og køre dem

            sql_select_query = """select * from Stockdb where Barcode = ?""" #Finder alt i productbatch tablet som matcher variablen til barcode kolonnen 
            print("batch-barcode: ", BatchData.Barcode)         
            cursor.execute(sql_select_query, (BatchData.Barcode,))                  #Nu køre vi querien med vores tuple variabler
            records = cursor.fetchall()                                             #Her hiver den så alt ud af databasen og sætter records variablen lig med det
            print("Printing ID ", BatchData.Barcode)
            for row in records:                                 #For loopet her køre lige så mange gange den har fået rækker ud af tabellen
                if(BatchData.Barcode == str(row[0])):           #Kigger på om det kolonne 1 i rækkerne matcher vores barcode variable i batchdata
                    print("Vi har det batch")
                    BatchData.stockoptionbatch = True           #Hvis den matcher sætter den stockoptionbatch til True for at indikere vi allerede har det batch på lager
                    BatchData.Quantity = row[7]                 #Samtidig med den tager antallet der er på lager
                else:                                             
                    print("row0 = ", row[0])
                    print("Vi har ikke det batch")
                    BatchData.stockoptionbatch = False          #Hvis den barcode ikke matcher så sætter den stockoptionbatch til False for at vise vi ikke har det batch på lager
            cursor.close()                                      #Derefter lukker vi cursor metoden. Hvilket for os er forbindelsen til databasen
        except sqlite3.Error as error:                          #Hvis der sker en fejl udprinter vi fejlbeskeden
            print("Failed to read data from sqlite table", error)
        finally:                                                #Til sidst kigger den på om den har en forbindelse til en database. Hvis den har det lukker den forbindelsen
            if sqliteConnection:
                sqliteConnection.close()
    # hvis nyt antal ikke er 0 plus antal og nytantal sammen
    #ellers minus antal med 1
    #kør sql update funktion med nyt antal  
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

#indsæt funktion til at sætte kategorierne ind i databasen
    def indsæt():
        try:                                                   #Vi har nedenstående inde i en try så programmer ikke lukker hvis der sker en fejl
            sqliteConnection = sqlite3.connect('Storedb.db')     #Opretter forbindelse til batch.db
            cursor = sqliteConnection.cursor()                 #cursor er en instance hvor man kan tilsutte sqlite metoder og køre dem
        

            sqlite_insert_query = """INSERT INTO Stockdb                    
                                (Barcode, Product, EAN13, EAN6, Date, Batch, Category, Price, Quantity) 
                                VALUES 
                                (?,?,?,?,?,?,?,?)"""                                                                                                                        #Her indsætter vi i databasen. Og vi definere kolone navnene vi gerne vil sætte ind på og derefter de værdier vi gerne vil sætte ind. Det gør vi ved ? for at vise det variabler som vi definere senere
            tuple1 = (str(BatchData.Barcode), BatchData.Product, BatchData.EAN13, BatchData.EAN6, BatchData.Date, BatchData.Batch, BatchData.Category, BatchData.Price, BatchData.Quantity,) #Spørgsmålstegnene ovenover betyder at vi har variabler. Her laver vi en tuple med de værdier vi gerne vil bruge
            print("row værdi: ", tuple1)
            cursor.execute(sqlite_insert_query, tuple1)                                                                                                                     #Nu køre vi querien med vores tuple variabler
            sqliteConnection.commit()                                                                                                                                       #Og vi skal commit for at den endelige ændring sker
            print("Record inserted successfully into Batch, Productbatch table ", cursor.rowcount)
            cursor.close()                                                                                                                                                  #Derefter lukker vi cursor metoden. Hvilket for os er forbindelsen til databasen

        except sqlite3.Error as error:                  #Hvis der sker en fejl udprinter vi fejlbeskeden
            print("Failed to insert data into productbatch table", error)
        finally:                                        #Til sidst kigger den på om den har en forbindelse til en database. Hvis den har det lukker den forbindelsen
            if sqliteConnection:
                sqliteConnection.close()


