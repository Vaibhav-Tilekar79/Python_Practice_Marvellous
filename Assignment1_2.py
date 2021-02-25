'''
Que -> Write a program which contains one function named as ChkNum() which accept one
	   parameter as number. If number is even then it should display “Even number” otherwise
	   display “Odd number” on console.

Output -> E.g -> i/p = 11	
				o/p = Odd Number
'''

def ChkNum(var):
	if var % 2 == 0:
		print("The number is even.")
	else:
		print("The number is odd.")

def main():
	num = int(input("Enter the number :"))
	ChkNum(num)

if __name__=="__main__":
	main()