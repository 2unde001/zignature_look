an_letters = "aefhilmnorsxAEFHILMNORSX"

# Ask for user input
word = input("I will cheer for you! Enter a word: ")
times = int(input("Enthusiasm level (1-10): "))


for char in word:

    #check if the character is inside the letter
    if char in an_letters:
        print("Gime me an " + char + "! " + char)
    else:
        print("Give me a " + char + "! " + char)

# for loop that print how may time to print user input

print("What does that spell?")
for i in range(times):
    print(word, "!!!")
