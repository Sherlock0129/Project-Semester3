num = int(input("Enter a number: "))
res = 1
for i in range(1,num + 1):
	res *= i
print(f"The factorial of {num} is : {res}")
