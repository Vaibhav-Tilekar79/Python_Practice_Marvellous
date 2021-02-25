'''
Que -> Write a program which accept number from user and check whether that number is positive or
	   negative or zero.

E.g -> Input : 11 Output : Positive Number
	   Input : -8 Output : Negative Number
	   Input : 0 Output : Zero
'''

def ChkNum(value):
	if (value == 0):
		print("The number {} is ZERO.".format(value))
	elif (value >= 1):
		print("The number {} is POSITIVE.".format(value))
	else:
		print("The number {} is NEGATIVE.".format(value))

def main():
	IntNum = int(input("Enter the number: "))
	ChkNum(IntNum)

if __name__=="__main__":
	main()