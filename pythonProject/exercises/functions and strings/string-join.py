str1 = "I am 25 years and 10 months old"
new = "".join(item for item in str1 if item.isdigit())
print(new)