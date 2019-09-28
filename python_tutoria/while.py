from camelcase import CamelCase
# would capitalize the first letter
c = CamelCase()

number = 1

# print odd number
while number < 1500:
    if number % 2 != 0:
        print(number)
    number += 1


# print even number
while number < 1500:
    if number % 2 == 0:
        print(number)
    number += 1

# ADD USER INPUT INTO THE EMPTY LIST
L = []
while len(L) < 5:
    new_name = input("Please add a new name: ").strip()
    L.append(c.hump(new_name))
print("Sorry list if full")
print(L)

x = 34 - 23
y = "Hello"
z = 3.45

if z == 3.45 or y == "Hello":
    x = x + 1
    y = y + " word"
print(x)
print(y)


