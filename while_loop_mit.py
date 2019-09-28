
# num = 0
# while num <= 5:
# 	print(num)
# 	num +=1

# print(num)


x  = int(input("Enter an Integer :"))

ans = 0
while ans**3 < abs(x):
	ans = ans + 1
if ans**3 == abs(x):
	if x < 0:
		print("You entered a negative number")
		ans = -ans
	print("Cube root of " + str(x) + " is " + str(ans))
else:
	print(str(x) + " is not a perfect cube")

