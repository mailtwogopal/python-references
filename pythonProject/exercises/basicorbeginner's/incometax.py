def calcIncTax(salary):
    totalInterest = 0
    if salary <= 10000:
        roi = 0
        totalInterest = 0
    elif salary > 10000 & salary <= 20000:
        roi = 0.1
        totalInterest = totalInterest + salary * 0.1
    else:
        roi = 0.2 + 0.1
        totalInterest = totalInterest + (salary * roi)
    return totalInterest


print(calcIncTax(9999))
print(calcIncTax(10000))
print(calcIncTax(10001))
print(calcIncTax(19999))
print(calcIncTax(20000))
print(calcIncTax(20001))
print(calcIncTax(25000))