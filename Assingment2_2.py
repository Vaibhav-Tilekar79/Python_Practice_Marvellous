'''
Que -> Write a program which accept one number and display below pattern.

E.g -> Input : 5
       Output : * * * * *
				* * * * *
				* * * * *
				* * * * *
				* * * * *
'''				
def pattern1(nos):
	for i in range(nos):
		print("*""\t"*nos)

def main():
	IntNum = int(input("Enter the number: "))
	pattern1(IntNum)

if __name__=="__main__":
	main()