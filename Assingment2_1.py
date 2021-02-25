'''
Que -> Create on module named as Arithmetic which contains 4 functions as Add() for addition, Sub()
	   for subtraction, Mult() for multiplication and Div() for division. All functions accepts two
	   parameters as number and perform the operation. Write on python program which call all the
	   functions from Arithmetic module by accepting the parameters from user.
'''

from Arithmetic import *

def main():
	int1 = int(input("Enter the first number: "))
	int2 = int(input("Enter the second number: "))

	retAdd = Addition(int1,int2)
	print("The Addition of {} and {} is {}.".format(int1,int2,retAdd))

	retSub = Substraction(int1,int2)
	print("The substraction of {} and {} is {}.".format(int1,int2,retSub))

	retMul = Multiplication(int1,int2)
	print("The multiplication of {} and {} is {}.".format(int1,int2,retMul))

	retDiv = Division(int1,int2)
	print("The division of {} and {} is {}.".format(int1,int2,retDiv))

if __name__=="__main__":
	main()