# In practice we define tuple as:
our_tuple = [1, 2, 3, 4, "A", "B", "C"]
print(our_tuple)

# print index from 0 to 2
print(our_tuple[0:3])

# tuple is immutable (Cannot be change after it's created in like List which can be change)
# example

my_list = [1, 9, 4, 280, 45]
my_list[3] = 10
print(my_list)

# Change tuple index after it was create
# our_tuple[3] = 10  error message display : tuple doesn't support item assignment
# print(our_tuple)

# Assign list to tuple function
A = [1, 2, 3]
tuple(A)
print(A)

# Assign multiple variables to tuple as:
(A, B, C) = 1, 2, 3
print(A)
print(B)
print(C)

# We can do the same thing for list as:
(D, E, F) = 4, 5, 6

print(D)
print(E)
print(F)

print(my_list[1:3])


