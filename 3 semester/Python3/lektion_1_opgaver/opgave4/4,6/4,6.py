for i in range(0,31):
    if(i % 5 == 0 and i % 3 == 0 ):
        print("FizzBuZZ")
    elif(i % 5 == 0 ):
        print("Buzz")
    elif(i % 3 == 0 ):
        print("Fizz")
    else:
        print(i)
        