'''
Que -> Write a recursive program which accept number from user and return
summation of its digits.
E.g -> Input : 879
	   Output: 24
'''

def Add_Digit(no):
	if (no == 0):
		return 0
	else:
		return (no % 10 + Add_Digit(int(no / 10)))

def main():
	value = int(input("Enter the value : "))

	ret = Add_Digit(value)

	print("Addition is : ",ret)

if __name__ == "__main__":
	main()