print("Please think of a number between 0 and 100!")
low = 0
high = 100
secret_guess = 68

guessing = False
while not guessing :
    user_input = (low + high)//2

    print("is your secret number? " + str(round(user_input)))
    you_guess = input("Enter 'h' to indicate the guess is too high."+"h"
    " Enter 'l' to indicate the guess is too low."
    "Enter 'c' to indicate I guess correctly")

    if you_guess == "h":
        high = user_input 
        print("guess correctly. " + you_guess)    
    elif you_guess == "l":
        low = user_input
        print("guess correctly. " + you_guess)
    elif (you_guess == "c") and round(user_input) == secret_guess:
        print("guess correctly. " + you_guess)
        guessing = True
    else:
        print("Sorry, I did not understand your input")
print("Game over. Your secret number was:", round(user_input))

