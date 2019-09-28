# Nested if else statement
a = 8
b = 8
if a < b:
    print(a , "is less than b")
else:
    if b == a:
        print(b, "is eqaul to", a)
    else:
        pass
    
# name of the person
# height of the person
# person weight
# bmi formula =  weight(kg)/ height**2

name = "Smith"
person_height = 80
person_weight_kg = 90
bmi = person_weight_kg / (person_height**2)
print("bmi: "+ str(bmi))

if bmi < 25:
    print(name, "is not overweight")
else:
    print(name, "is overweight")

# input user
# input person weight
# input person height
# calculate bmi formula =  weight(kg)/ (height**2)

#name = input(">: ")
#person_weight_kg = float(input("What is your weight?: "))
#person_height = float(input("What is your height?:  "))
bmi = person_weight_kg / (person_height**2)


if bmi < 15:
    print("Very severely underweight")
elif bmi == 15 and bmi <= 16:
    print("severely underweight")
elif bmi == 16 and bmi <= 18.5:
    print("Underweight")
elif bmi == 18.5 and bmi <= 25:
    print("Normal(healthy weight)")
elif bmi == 25 and bmi <= 30:
    print("Overweight")
elif bmi == 30 and bmi <= 35:
    print("Moderately Obese")
elif bmi == 35 and bmi <= 40:
    print("Severely obese")
else:
     print("Very severely obese")



x1 = 25
epsilon1 = 0.01
step1 = 0.1
guess1 = 0.0

while abs(guess1**2 -x1) >= epsilon1:
    if guess1 <= x1:
        guess1 += step1
    else:
        break
if abs(guess1**2 - x1) >= epsilon1:
    print("failed")
else:
    print("succeesded: " + str(guess1))

# This test would fail
x1 = 23
epsilon1 = 0.01
step1 = 0.1
guess1 = 0.0

while abs(guess1**2 -x1) >= epsilon1:
    if guess1 <= x1:
        guess1 += step1
    else:
        break
if abs(guess1**2 - x1) >= epsilon1:
    print("failed")
else:
    print("succeesded: " + str(guess1))


# This code would be in infinity loop
# x = 25
# epsilon = 0.01
# step = 0.1
# guess = 0.0

# while guess <= x:
#     if abs(guess**2 - x) >= epsilon:
#         guess += step
# if abs(guess**2 - x) >= epsilon:
#     print("failed")
# else:
#     print("succeesded: " + str(guess))