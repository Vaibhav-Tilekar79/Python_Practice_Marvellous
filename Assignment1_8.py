'''
Que -> Write a program which accept number from user and print that number of “*” on screen.

E.g -> Input : 5 Output : * * * * *
'''

def StarPrnt(nos):
	print("*""\t"*nos)

def main():
	IntNos = int(input("Enter the number: "))
	StarPrnt(IntNos)

if __name__=="__main__":
	main()