from random import choice
# do something 5 times
# range() function take two argument :[START], STOP
# for i in range(20, 41):
#     print(i)

count = 0
for number in range(1, 4):
    # new_count = old_count + number
    count = count + number

    # It should be 6


# print(count)


# write a function that sum all element of the list and return them
def sum_list(my_list):
    count1 = 0
    for number1 in my_list:
        count1 = count1 + number1
    return count1


assert sum_list([1, 2, 3]) == 6
assert sum_list([1, 2, 3, 4]) == 10
print(sum_list([1, 2, 3]))


# Write a function that take a number and square it

def square_number(my_number):
    return my_number ** 2


def square_number_test():
    assert square_number(2) == 4
    assert square_number(4) == 16
    assert square_number(10) == 100
    assert square_number(6) == 36


print("Square number assertion mut be true")


def is_even_number(check_even_number):
    if check_even_number % 2 == 0:
        return True
    else:
        return False


print(is_even_number(10))


def test_is_even_number():
    assert is_even_number(10) == True
    assert is_even_number(3) == False
    assert is_even_number(8) == True
    assert is_even_number(100) == True
    assert is_even_number(101) == False
    print("EVEN NUMBER TEST WORK AS EXPECTED")


test_is_even_number()


# Check the odd number
def is_odd_number(check_odd_number):
    if check_odd_number % 2 != 0:
        return True
    else:
        return False


print(is_odd_number(10))


def test_is_odd_number():
    assert is_odd_number(10) == False
    assert is_odd_number(3) == True
    assert is_odd_number(8) == False
    assert is_odd_number(100) == False
    assert is_odd_number(101) == True
    print("ODD NUMBER TEST WORK AS EXPECTED")


test_is_odd_number()


# check length of a string
def string_length(my_string_length):
    tracker = 0
    for i in my_string_length:
        tracker += 1
    return tracker


# print(len(string_length("heloo")))

def test_string_length():
    assert string_length("hello!") == 6
    assert string_length("banana") == 6
    assert string_length("8") == 1
    assert string_length("funnyguys") == 9
    assert string_length("101") == 3
    print("STRING LENGTH TEST WORK AS EXPECTED")


test_string_length()


#  print the last letter of the string
def string_last_letter(my_last_letter):
    return my_last_letter[-1]


def test_string_last_letter():
    assert string_last_letter("hello!") == "!"
    assert string_last_letter("banana") == "a"
    assert string_last_letter("8") == "8"
    assert string_last_letter("funnyguys") == "s"
    assert string_last_letter("101") == "1"
    print("STRING LAST LETTER TEST WORK AS EXPECTED")


test_string_last_letter()


# Function that take take two number and return the bigger one

def return_bigger_number(small_number, big_number):
    if small_number < big_number:
        return big_number
    else:
        return small_number


def test_bigger_number():
    assert return_bigger_number(1, 2) == 2
    assert return_bigger_number(10, 20) == 20
    assert return_bigger_number(20, 10) == 20
    assert return_bigger_number(10, 10) == 10
    assert return_bigger_number(2, 1) == 2
    assert return_bigger_number("a", "b") == "b"
    print("BIGGER NUMBER WORKED EXPECTED")


test_bigger_number()


# Function that take three number and return the biggest one

def return_biggest_number(first_number, second_number, last_number):
    if first_number != second_number and first_number > last_number:
        return first_number
    elif first_number != last_number and first_number > last_number:
        return first_number
    elif second_number != first_number and second_number > last_number:
        return second_number
    elif second_number != last_number and second_number > last_number:
        return second_number
    elif last_number != first_number and last_number > first_number:
        return last_number
    elif last_number != second_number and last_number > second_number:
        return last_number
    else:
        return first_number


def test_biggest_number():
    assert return_biggest_number(1, 3, 2) == 3
    assert return_biggest_number(30, 10, 20) == 30
    assert return_biggest_number(20, 10, 30) == 30
    assert return_biggest_number(2, 1, 9) == 9
    assert return_biggest_number("a", "a", "b") == "b"
    print("BIGGEST NUMBER DISPLAY AS EXPECTED")


test_biggest_number()


def bigger_guy(num1, num2):
    # find bigger between num1 and num2
    # find biggest num between bigger(num1 and num2) and num3
    if num1 > num2:
        return num1
    else:
        return num2


def biggest_guy(num1, num2, num3):
    # use built in max function
    # return max(num1, num2, num3)
    return bigger_guy(bigger_guy(num1, num2), num3)


def test_biggest_number():
    assert biggest_guy(1, 3, 2) == 3
    assert biggest_guy(30, 10, 20) == 30
    assert biggest_guy(20, 10, 30) == 30
    assert biggest_guy(2, 21, 9) == 21
    assert biggest_guy("a", "a", "b") == "b"
    print("BIGGEST NUMBER DISPLAY AS EXPECTED")


test_biggest_number()


def choice_to_number(choice):
    my_list = {
        1: "Usain",
        2: "Me",
        3: "Tunde"
    }
    # my_number = int(input("Enter your choice number"))
    return my_list[choice]


# print(choice_to_number(1))


def number_to_choice(race_number):
    my_list2 = {
        "Usain": 1,
        "Me": 2,
        "Tunde": 3
    }

    # race_number = input("Enter your choice of number between 1 and 3")
    return my_list2[race_number]


# print(number_to_choice("Usain"))

def test_choice_to_number():
    assert choice_to_number(1) == "Usain"
    assert choice_to_number(2) == "Me"
    assert choice_to_number(3) == "Tunde"


def test_number_choice():
    assert number_to_choice("Usain") == 1
    assert number_to_choice("Me") == 2
    assert number_to_choice("Tunde") == 3


def test_all():
    test_choice_to_number()
    test_number_choice()
    print("ALL MY CODE SHOULD PASS")


test_all()

s = "Hello World"
count = 0
for char in s:
    count = count + 1
print(count)

number = 2
while number <= 2:
    print(number)
    number += 1

emp_time = 1.5
try:
    hrs = float(input("Enter Hours: "))
    rate = float(input("Enter Rate: "))
    if hrs > 40:
        var = rate * emp_time + rate
        total_hrs = var + hrs * rate
        print(total_hrs)
except:
    print("Error, please enter numeric input")

score = float(input("Enter score between 0.0 to 1.0: "))
for score in range(10):
    print(score)

# if score >= 0.9:
#     print("A")
# elif score >= 0.8:
#     print("B")
# elif score >= 0.7:
#     print("C")
# elif score <= 0.6:
#     print("D")
# else:
#     print("Bad Score")



