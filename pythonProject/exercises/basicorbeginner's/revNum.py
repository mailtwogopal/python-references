def reverse(num):
    num = str(num)
    if num == num[::-1]:
        print("true")
    else:
        print("not true")


reverse(1221)
reverse(123)
reverse(98667)