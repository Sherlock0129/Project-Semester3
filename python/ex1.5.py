num = int(input("Enter a number:"))
temp = num
res = 1
while temp > 0:
	res *= temp
	temp -= 1
print(f"The factorial of {num} is : {res}")
