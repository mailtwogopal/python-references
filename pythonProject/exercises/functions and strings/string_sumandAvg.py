import  re
str1 = "English = 78 Science = 83 Math = 68 History = 65"
ls = re.findall(r'\d+', str1)
addition = 0
for i in ls:
    addition = addition + int(i)
print(addition)
avg = addition/int(len(ls))
print(avg)
