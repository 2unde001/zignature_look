# Dictionary declaration
# DICT[key] --> value
# {key1: value1, key2: value2}
students = {"Alex": 25, "Bob": 27, "Ayo": 30, "Tinuola": 80}
print(students["Tinuola"])

# assigning another
students["Fred"] = 25
print(students["Fred"])
del students["Fred"]
# print(students["Fred"]) would have delete Fred from dictionary
# Get all the keys in the dictionary :
print(students.keys())

# accessing dictionary key as:
a = list(students.keys())
print(a[1])

# Accessing the keys value by converting dictionary to list as:
print(students.values())
print(list(students.values())[1:])

# Dictionary value or element cannot be access by index, only by their key
# Dictionary do not have an order
print(students)

phone_book = {

}




