import dbHandler
import EAN5conversion
import sqlite3
Barcodedic = {}
barcodelist1 = []
def barcode_Split(barcodes):
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
def identifier_check(barcode):
    dbHandler.BatchData.Barcode = str(barcode)
    for key, value in Barcodedic.items():
        print(key)
        if key == "17" or key == "16" or key == "15":
            dbHandler.BatchData.EAN6 = str(value)
            dbHandler.BatchData.Date =EAN5conversion.dato_konvertering(int(value))
        if key == "01":
            dbHandler.BatchData.EAN13 = str(value)
        if key == "37": #antal
            dbHandler.BatchData.NewQuantity = int(value)
        if key == "10": #batch
            dbHandler.BatchData.Batch = str(value)
    dbHandler.data_check()
barcode_Split('''(01)9615348218911(17)008203(10)ABCD6234(37)6(01)9615348218911(17)008206(10)ABC11225(37)6
(01)9615348218911(17)008252(10)ABCD8214(37)6(01)9615348218911(17)008237(10)ABC22125(37)6
(01)9615348218911(17)008254(10)ABCD6154(37)6(01)9615348218911(17)008238(10)ABC32125(37)6
(01)9615348218911(17)008232(10)ABCD1924(37)6(01)9615348218911(17)008239(10)ABC42125(37)6
(01)9615348218911(17)008252(10)ABCD9243(37)6(01)9615348218911(17)008215(10)ABC52125(37)6
(01)9615348218911(17)008272(10)ABCD2724(37)6(01)9615348218911(17)008225(10)ABC62125(37)6
(01)9615348218911(17)008282(10)ABCD7234(37)6(01)9615348218911(17)008235(10)ABC72125(37)6
(01)9615348218911(17)008232(10)ABCD7234(37)6(01)9615348218911(17)008245(10)ABC82125(37)6
(01)9615348218911(17)009252(10)ABCD2345(37)6(01)9615348218911(17)008255(10)ABC92125(37)6
(01)9615348218911(17)008452(10)ABCD8435(37)6(01)9615348218911(17)008265(10)AB102125(37)6
(01)9615348218911(17)008752(10)ABCD8325(37)6(01)9615348218911(17)008275(10)AB112125(37)6
(01)9615348218911(17)008232(10)ABCD7243(37)6(01)9615348218911(17)008285(10)AB122125(37)6
(01)9615348218911(17)008263(10)ABCD2545(37)6(01)9615348218911(17)008295(10)AB132125(37)6
(01)9615348218911(17)008259(10)ABCD7234(37)6(01)9615348218911(17)008242(10)AB142125(37)6
(01)9615348218911(17)008258(10)ABCD7234(37)6(01)9615348218911(17)008244(10)AB152125(37)6
(01)9615348218911(17)008257(10)ABCD2345(37)6(01)9615348218911(17)008234(10)AB162125(37)6
(01)9615348218911(17)008256(10)ABCD2435(37)6(01)9615348218911(17)008252(10)AB172125(37)6
(01)9615348218911(17)008255(10)ABCD7234(37)6(01)9615348218911(17)008299(10)AB182125(37)6
(01)9615348218911(17)008263(10)ABCD4354(37)6(01)9615348218911(17)008289(10)AB192125(37)6
(01)9615348218911(17)008282(10)ABCD4524(37)6(01)9615348218911(17)008279(10)AB202125(37)6
(01)9615348218911(17)008221(10)ABCD7234(37)6(01)9615348218911(17)008269(10)AB212125(37)6
(01)9615348218911(17)008287(10)ABCD2345(37)6(01)9615348218911(17)008267(10)AB222125(37)6
(01)9615348218911(17)008234(10)ABCD6234(37)6(01)9615348218911(17)008635(10)AB232125(37)6
(01)9615348218911(17)008723(10)ABCD8234(37)6(01)9615348218911(17)008535(10)AB242125(37)6
(01)9615348218911(17)008763(10)ABCD1823(37)6(01)9615348218911(17)008535(10)AB252125(37)6
(01)9615348218911(17)008123(10)ABCD9234(37)6(01)9615348218911(17)008275(10)AB262125(37)6
(01)9615348218911(17)008765(10)ABC43563(37)6(01)9615348218911(17)008735(10)AB272125(37)6
(01)9615348218911(17)008863(10)ABCD1556(37)6(01)9615348218911(17)008835(10)AB282125(37)6
(01)9615348218911(17)008171(10)AB456355(37)6(01)9615348218911(17)009235(10)AB292125(37)6
(01)9615348218911(17)008634(10)ABCD5555(37)6(01)9615348218911(17)010235(10)AB402125(37)6''')