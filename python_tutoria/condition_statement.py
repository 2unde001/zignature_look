# if 5 == 5:
#     print(True)
#
# worker_working_hours = 40
# if worker_working_hours > 40:
#     print("Long hours is not allowed!")
# elif worker_working_hours == 40:
#     print("Workers working hours is always 40 hours")
# elif worker_working_hours < 40:
#     print("Worker that work less than 40 hours must explained the reason to their supervisor")
# elif worker_working_hours >= 40:
#     print("Pay him his working hours")

math_homework = False
long_essay = False
math_homework and long_essay

poison = False
pizza = True

if poison or pizza:
    print("Always True")
else:
    print("False")

# rock scissors game

human = "rock"
computer = "scissors"
human_score = 0
oomputer_score = 0

if human == "rock" and computer == "scissors":
    human_score = 1
    print(human_score)
elif human == "rock" and computer == "bananas":
    computer_score = 0
    human_score = 0
else:
    print("You can't pick anything other than rock and scissors")

# if (CONDITION --> True)
#    THIS BLOCK OF CODE RUNS

if computer != "rock" or computer != "scissors" or computer != "paper":
    print("WRONG CHOICE, PICK AGAIN")

if computer != "rock" and computer != "scissors" and computer != "paper":
    print("WRONG CHOICE, PICK AGAIN")



