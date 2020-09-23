def checkIfSame(ls):
    length = len(ls)
    print(length)
    lastElem = ls[length - 1]
    print(lastElem)
    if ls[0] == lastElem:
        print("True")
    else:
        print("false")


checkIfSame([1, 2, 3, 4, 2, 1])
checkIfSame([10, 20, 30, 40])
checkIfSame(["hi", "test", "string", "hi"])
