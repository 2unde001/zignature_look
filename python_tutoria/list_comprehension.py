# It's a combination of variable, list, for loops and if statement to create a list
# in one line of code

# Create a list of even numbers
even_numbers = [x for x in range(1, 1001) if x % 2 == 0]
print(even_numbers)

# Create a list of odd numbers
odd_numbers = [x for x in range(1, 1001) if x % 2 != 0]
print(odd_numbers)

# Create list of strings
words = ["the", "quick", "brown", "fox", "jumps", "over", "lazy", "dog"]
# Create a nested list
answer = [[w.upper(), w.lower(), len(w)] for w in words]
print(answer)
