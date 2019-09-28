cube = 27

epsilon = 0.01
guess = 0
increament = 0.0001
num_quesses = 0

""" 
Guess and check the cube root of a number and increament my guess by 
0.0001 until guess number if close proximity the the cube
"""
while abs(guess**3 - cube) >= epsilon and guess <= cube:
    guess += increament
    num_quesses += 1
print("num_guesses =", num_quesses)
if abs(guess**3 - cube) >= epsilon:
    print("Failed on cube root of " , cube)
else:
    print(guess, "is close to the cube root of", cube)
