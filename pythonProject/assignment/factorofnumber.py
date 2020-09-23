x = 20
for i in range(1, x+1):
    if x % i == 0:
        print(i)
        if i % 2 == 0:
            print("even")
        else:
            print("odd")