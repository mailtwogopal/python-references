num = str(input())
# number = 1220
# newNum = 0
# while number > 0:
#     digit = number % 10
#     newNum = (newNum * 10) + digit
#     number = number // 10
# print(newNum)
# if newNum == num:
#     print(num, " is a palindrome")
# else:
#     print(num, " is not a palindrome")

# simple way to check if number is palindrome
# num = str(num)
print("after string ", num)
if num == num[::-1]:  # this will reverse the number starting from right
    print(num[::-1])
    print("number is palindrome")
else:
    print("not a palindrome")
