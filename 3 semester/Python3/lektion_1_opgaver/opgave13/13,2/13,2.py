def even(limit):
    a = (x for x in range(limit) if 0 == x % 2)
    for i in a:
        print(i)
even(10)