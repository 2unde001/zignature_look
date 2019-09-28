# use range function to loop trough on element
range(1, 10)
# [1, 2, 3, 4, 5,6,,7,8,9,10]

for number in range(1, 1001, 2):  # using steps here
    print(number)

# 0R List, tuple or Dict
for my_list in [1, 3, 5]:
    print(my_list)

# OR String
for letter in "abcde":
    print(letter)

vowel = 0
consonants = 0

for letter in "supercalifragilisticepialidicious":
    if letter.lower() in "aeiou":
        vowel += 1
    elif letter == " ":
        pass
    else:
        consonants += 1
print("There are {} vowels".format(vowel))
print("There are {} consonants".format(consonants))

# for loop with dictionaries

students = {
    "male": ["Tom", "Charlie", "Harry", "Frank"],
    "female": ["Sarah", "Huda", "Samantha", "Emily", "Elizabeth"]
}

# print all name that have letter a
for key in students.keys():
    for name in students[key]:
        if "a" in name:
            print(name)


def remove_even(lst):

    tracker = 0
    for i in range(len(lst)):
        tracker +=1
        even = i % 2 == 0
    return lst[even]

print(remove_even([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]))

