# slicing STEPS
# [START : STOP : STEP]
from typing import List, Union
import sys

data = "XBOX 360 | 150 | NEW "

# print XBOX 360
print(data[0:9])

# Print 150
print(data[11:14])

# print NEW
print(data[17:])

greeting = "Hi how are you doing,it is very nice to meet you."
# print all greeting contents
print(greeting[0:])

# print every other letter
print(greeting[0:-1:2])

# print you
print(greeting[45:])

# String reverse
hi = "hello"
print(hi[::-1])

# Using find method to locate element from the list
# find and index method would perform the same action
print("Index of element is: " + str(data.find("|")))

print("Index of element is: " + str(data.find("|", 10)))
print(data[data.find("|") + 1:data.find("|", 10)])

groceries = ["apple", "banana", 5, 6, "oranges", "pineapple"]
print(groceries)

# Using split method  as:
sentence_dash = "What-is-going-on?"
print(sentence_dash.split("-"))
print(sentence_dash[0])
# [START:STOP:STEP]
print(sentence_dash[:])
print(sentence_dash[:3])

# print going
print(sentence_dash[8:13])

# reverse list
print(groceries[:: -1])

# split individual element in the list
detail = data.split("|")
print(detail)
# get XBOX 360
product = detail[0]
print(product)

# get 150
price = detail[1]
print(price)

# Better way to perform above solution is:
product1, price1, condition1 = data.split("|")

print("product name is: " + str(product1))
print("price value is: " + str(price1))
print("product condition is: " + str(condition1))

x = int(input("Enter an integer: "))

if x % 2 == 0:
    print("")  # True block
    print("Even")
else:
    print("")
    print("Odd")

if x % 2 == 0:
    if x % 3 == 0:
        print("Divisible by 2 and 3")
    else:
        print("Divisible by 2 and not 3")
elif x % 3 == 0:
    print("Divisible by 3 and not by 2")

a = float(input("Enter a number for a :"))
b = float(input("Enter a number for b :"))

if a == b:
    print("a and b are equal")
    if b != 0:
        print("therefore, a / b is", a / b)
elif a < b:
    print("a is smaller")
else:
    print("thanks!")

x = 3
y = 10
if x == y:
    print("x are equal to y")
else:
    if x < y:
        print("x are less than y")
    else:
        print("x is greater than y")

inp = input("Enter Temperature: ")
try:
    fah = float(inp)
    cel = (fah - 32.0) * 5.0 / 9.0
    print(cel)
except:
    print('Please enter a number')
