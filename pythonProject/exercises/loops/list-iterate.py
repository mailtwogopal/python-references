list1 = [10, 15, 23, 20, 36, 40, 25, 145, 150, 155, 200, 483, 500]
for i in range(0, len(list1), 1):
    if list1[i] > 150:
        print("out of range for 150")
    else:
        if list1[i] % 5 == 0:
            print(list1[i])