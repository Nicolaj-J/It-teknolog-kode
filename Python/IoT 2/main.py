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