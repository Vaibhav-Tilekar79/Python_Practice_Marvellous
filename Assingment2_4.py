'''
Que -> Write a program which accept one number form user and return addition of its factors.

E.g -> Input : 12      Output : 16 (1+2+3+4+6)
'''

def factors(nos):
	sum = 0
	for i in range(1,nos):
		if (nos % i == 0):
			sum = sum + i
	print("The Addition of digit factors is: ",sum)
				
def main():
	IntNum = int(input("Enter the number: "))
	factors(IntNum)

if __name__=="__main__":
	main()
