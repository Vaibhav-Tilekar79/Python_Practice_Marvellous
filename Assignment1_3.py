'''
Que -> Write a program which contains one function named as Add() which accepts two numbers
       from user and return addition of that two numbers.

E.g -> Input : 11 5 
	   Output : 16
'''

def Add(var1,var2):
	return (var1+var2)
	

def main():
	num1 = int(input("Enter first numbers: "))
	num2 = int(input("Enter second number: "))

	SUM = Add(num1,num2)

	print("The addition of {} and {} is {}.".format(num1,num2,SUM))

if __name__=="__main__":
	main()