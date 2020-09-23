print("my", "name", "is", "Gopal", sep='***')

#  decimal to octal
print(oct(8))

#  controlling decimal points
dec = 456.23321
print('%.2f' % dec)  # to 2 decimal places
print("{0:.3f}".format(dec))  # to 3 decimal using format
print(round(dec, 2))  # using round

# accepting 5 float num from user
# floatlist = []
# for num in range(0,5):
#     number = float(input())
#     floatlist.append(number)
# print(floatlist)

# get 3 i/p from one call
str1, str2, str3 = input(str("enter the strings: ")).split()
print(str1, str2, str3)

# print data in certain format
totalMoney = 1000
quantity = 3
price = 450
# print("I have", totalMoney, " dollars so I can buy ", quantity, " footballs for ", price, " dollars")
# rather than writing as above line can be easily written as below
sentence = "I have {0} dollars so i can buy {1} footballs for {2:.2f} dollars"
print(sentence.format(totalMoney, quantity, price))