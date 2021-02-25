'''
Que -> Write a program which accept number from user and return addition of digits in that number.

E.g -> Input :  5187934 
	   Output : 37
'''

def Add(n):
	num = [int (x) for x in str(n)]
	result = sum(num)
	return result

def main():
	Num = (input("Enter the number: "))
	ret = Add(Num)
	print(ret)


if __name__=="__main__":
	main()