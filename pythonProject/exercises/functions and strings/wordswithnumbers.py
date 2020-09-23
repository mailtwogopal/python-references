str1 = "Emma25 is Data scientist50 and AI Expert"
new = str1.split()
print(new)
for item in new:
    if any(item.isalpha() )