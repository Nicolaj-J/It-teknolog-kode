


def cel2fahr(temp):
    T = temp *9/5+32
    return T
def fahr2cel(temp):
    T = (temp - 32)*5/9
    return T

x = float(input("skriv dit temperatur: "))

print("Temperatur fahrenheit",cel2fahr(x))
print(" Temperatur celsius",fahr2cel(x))