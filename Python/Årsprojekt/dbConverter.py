import dbHandler
import EAN5conversion
Barcodedic = {}
barcodelist1 = []
#Denne Funktion finder identifiers og værdier i stregkoden strengen
def barcode_Split(barcodes):
    if barcodes.count(')') > 0: #Kigger først efter om strengen indeholder parenteser. Hermed om den har identifiers
        Barcodelist = list(barcodes.split("(01)")) #Splitter strengen op ved hvert (01) og laver det til en liste
        Barcodelist.pop(0) #Sletter den første på listen
        print(Barcodelist)
        for x in Barcodelist: #Køre igennem for loopet så mange gange som der er "items" i listen. Altså identifiers i stregkoden
            barcode = "(01)"+ x #Siden der blev splittet ved (01) så er alle (01) slettet. Hermed Tilføjes (01) igen
            #Laver 2 variabler der bliver brugt når identifiers værdierne findes.
            val1 = -1 
            val2 = -1
            #Placere et ciffer i slutningen af stregkoden for at gøre det nemmere at få den sidste værdi ud
            barcode = barcode + '-'
            print(barcode)
            for i in range(1, barcode.count(')')+1): #Laver et for loop der køre igennem for hver identifier der er
                val1 = barcode.find('(', val1 + 1) #Finder positionen for "for" parentesen af identifieren. Den finder den identifier i rækken som matcher antal gange igennem for loopet 
                val2 = barcode.find(')', val2 + 1) #Finder positionen for "slut" parentesen af identifieren. Den finder den identifier i rækken som matcher antal gange igennem for loopet
                if(i == barcode.count('(')): #Hvis det er den sidste identifier i listen bliver slut værdien plusset med 3 for at få hele værdien med.
                    Barcodedic[barcode[val1 +1:val2]] = barcode[val2 +1:barcode.find('(', val1 + 3)] #Finder identifier og value som bliver placeret som key og value i dictionary
                elif(i < barcode.count('(')):#Hvis det er ikke den sidste identifier i listen bliver slut værdien plusset med 2 for at få hele værdien med.
                    Barcodedic[barcode[val1 +1:val2]] = barcode[val2 +1:barcode.find('(', val1 + 2)] #Finder identifier og value som bliver placeret som key og value i dictionary
            identifier_check(barcode)  
    else:
        print("Scannet en GTIN stregkode")    
#Scanner igennem keys og values for at finde de rigtige identifier værdier. 
def identifier_check(barcode):
    dbHandler.BatchData.Barcode = str(barcode)
    for key, value in Barcodedic.items(): #Laver et for loop der køre igennem lige så mange gange der er items i dictionariet
        print(key)
        if key == "17" or key == "16" or key == "15": #Dato
            dbHandler.BatchData.EAN6 = str(value)
            dbHandler.BatchData.Datotype = key
            dbHandler.BatchData.Date =EAN5conversion.dato_konvertering(int(value))
        if key == "01": #Gtin
            dbHandler.BatchData.EAN13 = str(value)
        if key == "37": #antal
            dbHandler.BatchData.NewQuantity = int(value)
        if key == "10": #batch
            dbHandler.BatchData.Batch = str(value)
    dbHandler.data_check()
