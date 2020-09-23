# easy way
num = 12354
num = str(num)
print(len(num))

# 2nd way
count = 0
num = int(num)
while num != 0:
    num = num // 10
    count += 1
print(count)
