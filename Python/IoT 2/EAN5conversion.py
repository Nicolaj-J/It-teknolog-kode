def dato_konvertering(EAN5):
    #Denne funktion laver EAN5 stregkoden om til en dato.
    dageår = 365
    skud = int(EAN5/365/4)
    start = 2000
    måned = 1
    år_dage = EAN5/dageår #Her finder vi hvilket år den udløber plus antal dage inde i året som er et komma tal
    år = int(år_dage) #Her skilder vi det ad
    dage = EAN5 - (år * 365 + skud)
    år = start + år
    månedlist = [31,29,31,30,31,30,31,31,30,31,30,31]
    for i in månedlist:
        if måned == 2 and år % 4 == 0:
            dage = dage - 29
            måned = måned +1
        elif måned == 2 and år % 4 != 0:
            dage = dage - 28
            måned = måned +1
        elif dage > i and måned != 2:
            dage = dage - i
            måned = måned +1
        else:
            break
    dato = f"{dage}/{måned}/{år}"
    return dato