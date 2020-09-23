num = 1000
items = []
for i in range(num, 3001):
    s = str(i)  # converting i to string - each number to string
    # below condition check if each index of string is even number or not
    if int(s[0]) % 2 == 0 and int(s[1]) % 2 == 0 and int(s[2]) % 2 == 0 and int(s[3]) % 2 == 0:
        items.append(s) # appending all digits to form number again
print(",".join(items))
