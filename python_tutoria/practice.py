# Using while loop to print even number
number = 1
while number <= 10:
    if number % 2 == 0:
        print(number)
    number += 1
print("Goodbye!")

# While loop to reverse order number
print("While Loop to reverse numbers order")
number = 12
print("Hello!")
while number >= 4:
    number -= 2
    print(number)

# While loop to add number between 1 to 13
print("While Loop to add numbers between 1 to 13")

total = 0
number = 1
while number <= 13:
    total += number
    number += 1
print(total)

print("<h1>FOR LOOP TO GET EVEN NUMBER </h1>")
for number in range(2, 12):
    if number % 2 == 0:
        print(number)
print("Goodbye!")

# for loop to reverse number order
print("<h1>FOR LOOP REVERSE NUMBER ORDER, 10, 8, 6, 4, 2 </h1>")
print("Hello!")
for count in range(10, 0, -2):
    print(count)

# for loop to Add number from 0 10 11
print("FOR LOOP ADD INDIVIDUAL NUMBER TOGETHER")
total_sum = 0
for i in range(0, 11):
    i += 1
    total_sum += i
print(total_sum)

for letter in "hola":
    print(letter)

count = 0
for letter in 'Snow!':
    print('Letter # ' + str(count) + ' is ' + str(letter))
    count += 1
    break
print(count)

# n = 10
# for n in range(5):
#     print(n)
#     print("Now" + n)

print("-----------------------------")
mystr = "6.00x"
for char in mystr:
    print(char)
print("done")

greeting = 'Hello!'
count = 0

for letter in greeting:
    count += 1
    if count % 2 == 0:
        print(letter)
    print(letter)

print('done')

school = 'Massachusetts Institute of Technology'
numVowels = 0
numCons = 0

for char in school:
    if char == 'a' or char == 'e' or char == 'i' \
            or char == 'o' or char == 'u':
        numVowels += 1
    elif char == 'o' or char == 'M':
        print(char)
    else:
        numCons -= 1

print('numVowels is: ' + str(numVowels))
print('numCons is: ' + str(numCons))

counter = 100
while counter >= 0:
    if counter > 0:
        print(counter)
    if counter == 0:
        print("Boom!")
    counter -= 1

x = int(input("Guess a number: "))
ans = 0

while ans * ans * ans < abs(x):
    ans = ans + 1
    print("current guess " + str(ans))
print("Last guess = " + str(ans))
print("ans * ans * ans = " + str(ans * ans * ans))

if ans * ans * ans == abs(x):
    if x < 0:
        print("You entered a negative number")
        ans = -ans
    print("Cube of " + str(x) + " is " + str(ans))

else:
    print(str(x) + " is not a perfect cube")

print("**************************")
cube = -27
for guess in range(cube + 1):
    if guess ** 3 >= abs(cube):
        break
    if guess ** 3 != abs(cube):
        print(str(cube) + " not a perfect cube")
    else:
     if guess ** 3 < 0:
        guess = -guess
    print("Cube root if " + str(cube) + " is " + str(guess))
