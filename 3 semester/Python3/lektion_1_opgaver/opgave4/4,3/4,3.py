

def subave(tal):
    y = 0
    for i in range(0,tal +1):
        y = y + i
    return y, tal

total, tal = subave(int(input("Write a number: ")))
print("Sum: ", total )
print("Average: ", total/tal)
