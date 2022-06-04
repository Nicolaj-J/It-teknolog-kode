import dbHandler
import EAN5conversion
Barcodedic = {}
barcodelist1 = []
def barcode_Split(barcodes):
    if barcodes.count(')') > 0:
        Barcodelist = list(barcodes.split("(01)"))
        Barcodelist.pop(0)
        print(Barcodelist)
        for x in Barcodelist:
            barcode = "(01)"+ x
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
            identifier_check(barcode)  
    else:
        print("Scannet en GTIN stregkode")     
def identifier_check(barcode):
    dbHandler.BatchData.Barcode = str(barcode)
    for key, value in Barcodedic.items():
        print(key)
        if key == "17" or key == "16" or key == "15":
            dbHandler.BatchData.EAN6 = str(value)
            dbHandler.BatchData.Datotype = key
            dbHandler.BatchData.Date =EAN5conversion.dato_konvertering(int(value))
        if key == "01":
            dbHandler.BatchData.EAN13 = str(value)
        if key == "37": #antal
            dbHandler.BatchData.NewQuantity = int(value)
        if key == "10": #batch
            dbHandler.BatchData.Batch = str(value)
    dbHandler.data_check()
