'''
Que -> Write a program which contains one function that accept one number from user and returns
	   true if number is divisible by 5 otherwise return false.

E.g -> Input : 8    Output : False
       Input : 25   Output : True
'''

def IsDiv(nos):
	if (nos % 5 == 0):
		return True
	else:
		return False

def main():
	num = int(input("Enter the number: "))
	ret = IsDiv(num)
	print(ret)

if __name__=="__main__":
	main()