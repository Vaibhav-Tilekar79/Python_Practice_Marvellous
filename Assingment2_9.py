'''
Que -> Write a program which accept number from user and return number of digits in that number.

E.g -> Input :  5187934 		
	   Output : 7
'''

def CntNum(n):
	icnt = 0
	while n > 0:
		n = n // 10
		icnt = icnt + 1
	return icnt

def main():
	Num = int(input("Enter the number: "))
	ret = CntNum(Num)
	print("The number of digits in a given number is: ",ret)

if __name__=="__main__":
	main()