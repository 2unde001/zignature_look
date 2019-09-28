x = 5 
ans= 0
iterateLeft = x

while (iterateLeft != 0):
    ans = ans + x
    iterateLeft = iterateLeft - 1
print(str(x) + "*" + str(x) + " = " + str(ans))

num = 10
for num in range(5):
    print(num)
print(num)

divisor = 2
for num in range(0, 10, 2):
    print(num/divisor)

count = 0
for letter in "Snow":
    print("Letter # "+ str(count) + " is " + str(letter))
    count +=1
    break
print(count)

for variable in range(20):
    if variable % 4 == 0:
        print(variable)
    if variable % 16 == 0:
        print("Foo!")

print("***********************************")
greeting = "Hello"
counter = 0

for char in greeting:
    counter += 1
    if counter % 2 == 0:
        print(char)
    print(char)

print("done")

print("************" +" Vowels" +" & "+ "Consonant" +" Numbers " + "************")
school = "Massachusetts Institute of Technology"
numVowels = 0
numCons = 0

for char_count in school:
    if char_count == "a" or char_count == "e" or char_count == "i" \
        or char_count == "o" or char_count == "u":
        numVowels += 1
    elif char_count == "o" or char_count == "M":
        print(char_count)
    else:
        numCons -= 1
print("numVowels is: "+ str(numVowels))
print("numCons is: " + str(numCons))

print("************" +" Find The Cube Root of an Input Number "+ "************")

x = int(input("Enter an Integer: "))
answer = 0

while answer**3 < abs(x):
   answer = answer + 1
if answer**3 != abs(x):
    print(str(x) + " is not a perfect cube")
else:
    if x < 0:
        answer = - answer
    print("Cube root of " + str(x) + " is "+ str(answer)) 

print("************" +" Guess a Number using for loop "+"************")

# cube = 28
# for guess in range(cube + 1):
#     if guess**3 >= abs(cube):
#         break
# if guess**3 != 0 abs(cube):
#     print(cube, "is not a perfect cube")
#         else:
# if cube < 0:
#         guess = -guess
#     print("Cube root of " + str(cube) + " is " + str(guess))


tracker = 0
phrase = "hello world"
for iteration in range(5):
    while True:
        tracker+= 1
        break
    print("Iteration " + str(iteration) + "; tracker is: "+str(tracker))
  
another_count = 0
phrase = "hello world"
for iteration in range(5):
    index = 0
    while index < len(phrase):
        another_count+= 1
        index+= 1
    print("Iteration " + str(iteration) + "; another count is "+ str(another_count))

string = "azcbobobegghaki"
string_count = 0
num_of_occurent = 0

for word in string:
   string_count = string.find("bob")
   if string_count >= 0:
       num_of_occurent += 1
       string_count = string[string_count + 1:]
print("Number of time bob occurs is: "+ str(num_of_occurent))


