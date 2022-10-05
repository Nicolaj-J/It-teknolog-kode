
def fibonacci(længde):
    numberlist = [0,1]
    while len(numberlist) < længde:
        numberlist.append(numberlist[-1]+numberlist[-2])
    return numberlist
print(fibonacci(10))
