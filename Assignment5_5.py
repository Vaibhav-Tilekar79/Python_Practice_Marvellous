'''
Que -> Write a recursive program which accept number from user and return its
	   factorial.

E.g -> Input :  5
	   Output : 120
'''

def Fact(no):
	if (no == 0 or no == 1):
		return 1
	else:
		return no*Fact(no-1)
		

def main():
	value = int(input("Enter the value : "))

	ret = Fact(value)

	print("The factorial is : ",ret)

if __name__=="__main__":
	main()