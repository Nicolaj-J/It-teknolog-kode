O = 5
l = 7


def MyFunc(a: int, b: int, c: int) -> (int, bool):
    if not c == None:
        return a * 3 + b * 4-c, True
    else:
        return 0, False


result, v = MyFunc(a=O, b=l, c=1)

print("result = %d" % (result))
