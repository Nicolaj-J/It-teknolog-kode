

def dato_konvertering(x):
    dageår = 365
    skud = x/365/4
    start = 2000
    måned = 1
    år_dage = start + x/dageår
    år, dage = int(år_dage), år_dage-int(år_dage)
    dage = int(dage*365-int(skud))

    if(dage > 31): #Januar
        dage = dage - 31
        måned = måned + 1
    if(dage > 29): #Februar
        if(år % 4 == 0):
            dage = dage - 29
            måned = måned + 1
        elif(år % 4 != 0):
            dage = dage - 28
            måned = måned + 1
    if(dage > 31): #Marts
        dage = dage - 31
        måned = måned + 1
    if(dage > 30): #April
        dage = dage - 30
        måned = måned + 1
    if(dage > 31): #Maj
        dage = dage - 31
        måned = måned + 1
    if(dage > 30): #Juni
        dage - 30
        måned = måned + 1
    if(dage > 31): #Juli
        dage = dage - 31
        måned = måned + 1
    if(dage > 31): #August
        dage = dage - 31
        måned = måned + 1
    if(dage > 30): #September
        dage = dage - 30
        måned = måned + 1
    if(dage > 31): #Oktober
        dage = dage - 31
        måned = måned + 1
    if(dage > 30): #november
        dage = dage - 30
        måned = måned + 1
    if(dage > 31): #December
        dage = dage - 31
        måned = måned + 1
    dato = f"{dage}/{måned}/{år}" 
    return dato

konvertering = dato_konvertering(8108)
print(konvertering)
