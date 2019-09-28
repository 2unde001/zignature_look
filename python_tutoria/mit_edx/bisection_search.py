import math
# Bisection search the square root

x = 25
epsilon = 0.01
numGuesses = 0
# set a low value
low = 0.0
# set a high value
high = x
# the half way between high and low guess / 2
ans = (high + low) / 2.0


while abs(ans**2 - x) >= epsilon:
    print("low = " + str(low) + " high = " + str(high) + " ans = " + str(ans))

    '''
    Increase the guess number by if if the cube root of answer
    minus x is greather than epsilon
    '''
    numGuesses += 1

    ''' 
    If answer is too small, move to the low part of range
    If answer is too high move to the high part of range"
    '''
    if ans**2 < x:
        low = ans              
    else:
        high = ans
    ans = (high + low) / 2.0
print("numberGuesses = " + str(numGuesses))
print(str(ans) + " is close to square root of " + str(x))

print("**************Cube Root*****************")

# Bisection search the cube root

cube = 27
epsilon = 0.01
numGuesses = 0
# set a low value
low = 0.0
# set a high value
high = cube
# the half way between high and low guess / 2
ans = (high + low) / 2.0


while abs(ans**3 - cube) >= epsilon:
    print("low = " + str(low) + " high = " + str(high) + " ans = " + str(ans))

    '''
    Increase the guess number by if if the cube root of answer
    minus x is greather than epsilon
    '''
    numGuesses += 1

    ''' 
    If answer is too small, move to the low part of range
    '''
    if ans**3 < cube:
        low = ans
    else:
        #    If answer is too high move to the high part of range"
        high = ans
    ans = (high + low) / 2.0 # make another guess
    numGuesses += 1
print("numberGuesses = " + str(numGuesses))
print(str(ans) + " is close to cube root of " + str(cube))


lo = 0
hi = 9
epi = 0.01
guess_num = 0

guess = (lo + hi)/2

my_guess= False
while(not my_guess):

    if guess < 0:
        lo = guess
    else:
        hi = guess
    

