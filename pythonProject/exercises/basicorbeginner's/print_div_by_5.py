def divisibleBy5(ls):
    for i in range(0, len(ls), 1):
        if ls[i] % 5 == 0:
            print(ls[i])


divisibleBy5([2, 4, 10, 13, 15, 21])
divisibleBy5([1, 4, 7, 25])
