def addandsub(int1, int2):
    c = int1 + int2
    if int1 > int2:
        d = int1 - int2
    else:
        d = int2 - int1
    return  c, d


print(addandsub(4, 21))