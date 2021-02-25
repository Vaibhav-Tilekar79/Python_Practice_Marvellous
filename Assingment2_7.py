'''
Que -> Write a program which accept one number and display below pattern.
	
E.g	-> Input :  5
	   Output : 1 2 3 4 5
			    1 2 3 4 5
			    1 2 3 4 5
			    1 2 3 4 5
			    1 2 3 4 5
'''

def pattern(num):
	for i in range(1,num+1):			#to decide rows.
		for j in range(1,num+1):		#to decide columns.
			print(j,"", end=" ")
		print("\r")	
def main():
	IntNum = int(input("Enter the number: "))
	pattern(IntNum)

if __name__=="__main__":
	main()