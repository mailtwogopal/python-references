for i in range(11):
    print(i)


# pattern printing
for j in range(7):
    for num in range(1, j):
        print(num, end='  ')
    print("\n")

# sum of all given num
number = 5
sumof = 0
for i in range(1, number+1, 1):
    sumof = sumof + i
print(sumof)

# multiplication table
givenNum = 7
for i in range(1, 13, 1):
    print(i, " * ", givenNum, " = ", i * givenNum)