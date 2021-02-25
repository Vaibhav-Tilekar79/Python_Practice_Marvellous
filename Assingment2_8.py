'''
Que -> Write a program which accept one number and display below pattern.

E.g -> Input : 5
	   Output : 1
				1 2
				1 2 3
				1 2 3 4
				1 2 3 4 5
'''

def NumPattern(n):
	for i in range(1,n+1):
		for j in range(1,i+1):
			print(j,"", end=" ")
		print("\r")

def main():
	Num = int(input("Enter the number: "))
	NumPattern(Num)

if __name__=="__main__":
	main()