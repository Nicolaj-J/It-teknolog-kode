#dHer opretter vi funktionen.
def myfirstfunction (arg1, arg2, arg3):
    #her returner vi specifikke ting
    return arg1 + arg2 + arg3

# print(myfirstfunction(10, 10, 10))

#her opretter man funktionen med et argument a
def retList(a):
    #her oprettier vi en liste
    list=[]
    #her tilføjer vi tal til listen. i kronologisk rækkefølge. Det gør vi ved at for loopet køre igennem så mange gange som a har af værdi
    for i in range(0, a):
        list.append(i)
    return list
#her sætter vi a værdi
a = retList(88)
# print(a)

#hvis vi ikke ved hvor mange argumenter vi skal have. Så sætter vi en stjerne foran.
def mysum(*args):
    result = 0
    for item in args:
        result += item
    return result
# print(mysum(312, 12312, 1231, 12))




