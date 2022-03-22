import sqlite3
class BatchData:
    Barcode = '' #fundet main
    Product= '' #fundet dbhandler
    EAN13 = '' #fundet main
    EAN5 = '' #fundet main
    Date = '' #fundet main
    Category = '' #fundet dbhandler
    Price = 0 #fundet dbhandler
    Quantity = 0 #fundet dbhandler
    stockoptionbatch = False #fundet dbhandler
    stockoptionproduct = False #fundet dbhandler
    NewQuantity = 0
def data_check():
    data_check_product()
    data_check_batch()
    batch_quantity()
    print("barcode: ", BatchData.Barcode)
    print("stockoptionproduct", BatchData.stockoptionproduct)
    print("stockoptionbatch", BatchData.stockoptionbatch)
    if(BatchData.stockoptionproduct == True and BatchData.stockoptionbatch == False):
        insert_data_batch()
    if(BatchData.stockoptionproduct == True and BatchData.stockoptionbatch == True):
        data_update_batch()
    batch_status_checker()
    batchdata_reset()
def data_update_batch():
    try:
        sqliteConnection = sqlite3.connect('batch.db')
        cursor = sqliteConnection.cursor()

        sql_update_query = """Update Productbatch set Quantity = ? where Barcode = ?"""
        data = (BatchData.Quantity, BatchData.Barcode)
        print(data)
        cursor.execute(sql_update_query, data)
        sqliteConnection.commit()
        print("Batch Updated successfully")
        cursor.close()

    except sqlite3.Error as error:
        print("Failed to update batch table", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
def insert_data_batch():
    try:
        sqliteConnection = sqlite3.connect('batch.db')
        cursor = sqliteConnection.cursor()
    

        sqlite_insert_query = """INSERT INTO Productbatch
                            (Barcode, Product, EAN13, EAN5, Date, Category, Price, Quantity) 
                            VALUES 
                            (?,?,?,?,?,?,?,?)"""
        tuple1 = (str(BatchData.Barcode), BatchData.Product, BatchData.EAN13, BatchData.EAN5, BatchData.Date, BatchData.Category, BatchData.Price, BatchData.Quantity)
        print("row værdi: ", tuple1)
        cursor.execute(sqlite_insert_query, tuple1)
        sqliteConnection.commit()
        print("Record inserted successfully into Batch, Productbatch table ", cursor.rowcount)
        cursor.close()

    except sqlite3.Error as error:
        print("Failed to insert data into productbatch table", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
def batch_quantity():
    if(BatchData.NewQuantity != 0):
        BatchData.Quantity = BatchData.Quantity + BatchData.NewQuantity
    else:
        print(BatchData.Quantity)
        BatchData.Quantity = BatchData.Quantity - 1
        print(BatchData.Quantity)
        print("Ændret antal")
def batch_status_checker():
    try:
        sqliteConnection = sqlite3.connect('batch.db')
        cursor = sqliteConnection.cursor()

        sql_update_query = """DELETE from Productbatch where Quantity <= ?"""
        cursor.execute(sql_update_query, (0,))
        sqliteConnection.commit()
        print("Record deleted successfully")

        cursor.close()

    except sqlite3.Error as error:
        print("Failed to delete reocord from a sqlite table", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print("sqlite connection is closed")
def data_check_batch():
    try:
        sqliteConnection = sqlite3.connect('batch.db')
        cursor = sqliteConnection.cursor()

        sql_select_query = """select * from Productbatch where Barcode = ?"""
        print("batch-barcode: ", BatchData.Barcode)
        cursor.execute(sql_select_query, (BatchData.Barcode,))
        records = cursor.fetchall()
        print("Printing ID ", BatchData.Barcode)
        for row in records:
            if(BatchData.Barcode == str(row[0])):
                print("Vi har det batch")
                BatchData.stockoptionbatch = True
                BatchData.Quantity = row[7]
                BatchData.Quantity = row[6]
            else:
                print("row0 = ", row[0])
                print("Vi har ikke det batch")
                BatchData.stockoptionbatch = False
        cursor.close()
    except sqlite3.Error as error:
        print("Failed to read data from sqlite table", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
def data_check_product():
    try:
        sqliteConnection = sqlite3.connect('product.db')
        cursor = sqliteConnection.cursor()

        sql_select_query = """select * from products where EAN13 = ?"""
        cursor.execute(sql_select_query, (BatchData.EAN13,))
        records = cursor.fetchall()
        print("Printing ID ", BatchData.EAN13)
        for row in records:
            print(row[0])
            print("EAN13: ", BatchData.EAN13)
            if(BatchData.EAN13 == row[0]):
                print("Vi har produktet")
                BatchData.stockoptionproduct = True
                BatchData.Product = row[1]
                BatchData.Category = row[2]
                BatchData.Price = row[3]
            else:
                BatchData.stockoptionproduct = False
                print("Vi har ikke produktet")
        cursor.close()
    except sqlite3.Error as error:
        print("Failed to read data from sqlite table", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
def batchdata_reset():
    BatchData.Barcode = '' 
    BatchData.Product= '' 
    BatchData.EAN13 = ''
    BatchData.EAN5 = '' 
    BatchData.Date = '' 
    BatchData.Category = ''
    BatchData.Price = 0 
    BatchData.Quantity = 0
    BatchData.stockoptionbatch = False 
    BatchData.stockoptionproduct = False
    BatchData.NewQuantity = 0
    print("Batchdata is now reset")
def insert_data_products():
    try:
        sqliteConnection = sqlite3.connect('product.db')
        cursor = sqliteConnection.cursor()
        sqlite_insert_query = """INSERT INTO Products
                            (EAN13, Product,Category, Price) 
                            VALUES 
                            (9615348218911, 'Big Corny - Chocolate & salted caramel', 'Mejeri', 10)"""
        
        cursor.execute(sqlite_insert_query)
        sqliteConnection.commit()
        print("Record inserted successfully into SqliteDb_developers table ", cursor.rowcount)
        cursor.close()
    except sqlite3.Error as error:
        print("Failed to read data from sqlite table", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()