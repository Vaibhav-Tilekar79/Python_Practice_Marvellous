'''
Que -> Write a program which accept one number and display below pattern.

E.g -> Input : 5
	   Output : * * * * *
				* * * *
				* * *
				* *
				*
'''				

def pattern(n):
       for i in range(n, 0, -1):
            for j in range(0, i):
                print("* ", end=" ")
            print("\r")

			
def main():
	Num = int(input("Enter the number: "))
	pattern(Num)

if __name__=="__main__":
	main()
