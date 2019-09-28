cube = 8
for guess in range(abs(cube) + 1):
    if guess**3 >= abs(cube):
        break
if guess**3 != abs(cube):
    print(guess, "is not a perfect cube")
else:
    if cube < 0:
        guess -= guess
        print("Cube root of "+str(cube) + " is " + str(guess))


#Guessing cube root of usr input
ans = 0
neg_flag =  False
x = int(input("Enter an Integer: "))
if x < 0:
    neg_flag = True
while ans** 2 < x:
    ans+= 1
if ans**2 == x:
    print("Square root of", x, "is", ans)
else:
    print(x, "is not a perfect square")
    if neg_flag:
        print("Just checking... did you mean", -x, "?")

    

#For Loops 
# for loop have a loop variable that iterate over a set of values
# for var in range(4):
#     <expression>
#     var iterates over values 0,1,2,3
#     expressions inside loop executed with each value for var

s = "abcdefgh"
#Iterate through each element os the string s
for char in s:
    if char == "i" or char == "u":
        print("There is an i or u")

