def dato_konvertering(x):
    #Denne funktion laver EAN5 stregkoden om til en dato.
    dageår = 365
    skud = x/365/4
    start = 2000
    måned = 1
    år_dage = start + x/dageår #Her finder vi hvilket år den udløber plus antal dage inde i året som er et komma tal
    år, dage = int(år_dage), år_dage-int(år_dage) #Her skilder vi det ad
    dage = int(dage*365-int(skud)) #Her ganger vi komma tallet med 365 for at finde antal dage inde i året hvorefter vi tager højde for skudår
    
    #Disse if statements går bare igennem og kigger på om vi har flere dage en der er i hver enkelt måned. Hvorefter den trækker det antal dage
    #fra og lægger 1 måned til
    if(dage > 31): #Januar
        dage = dage - 31
        måned = måned + 1
    if(dage > 28): #Februar
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
    dato = f"{dage}/{måned}/{år}" #her sammensætter vi datoen
    return dato #Og returnere den