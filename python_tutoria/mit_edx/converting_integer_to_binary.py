num = 11
if num < 0:
    is_Negetive = True
    num = abs(num)
else:
    is_Negetive = False
result = ""
if num == 1:
    result = "0"
while num > 0:
    result = str(num%2) +result
    num = num  // 2
if is_Negetive:
    result = "-" + result
print(result)

"""
Coverting float number to binary
"""

x= float(input("Enter a decimal number between 0 and 1: "))

p = 0
while ((2**p)*x)%1 != 0:
    print("Remainder = " + str((2**p)*x - int((2**p)*x)))
    p+= 1

number = int(x*(2**p))

result1 = ""
if number == 0:
    result1 = "0"
while number > 0:
    result1 = str(number%2) + result1
    number = number//2
for i in range(p - len(result1)):
    result1 = "0" + result1

result1 = result1[0:-p] + "." + result1[-p:]
print("The binary representation of the decimal "+ str(x) +" is "+ str(result1))