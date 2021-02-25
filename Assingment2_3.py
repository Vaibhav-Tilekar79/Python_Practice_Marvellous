'''
Que -> Write a program which accept one number from user and return its factorial.

E.g -> Input : 5 Output : 120
'''

def fact(nos):
	factorial = 1

	if (nos < 0):
		print("Enter valid number.")

	elif (nos == 0):
		print("The factorial is 1.")

	else:
		for i in range(1, nos+1):
			factorial = factorial * i
		return factorial		

def main():
	IntNum = int(input("Enter the number for which you want factorial: "))
	ret = fact(IntNum)
	print("The factorial is: ",ret)

if __name__=="__main__":
	main()