'''
Que -> Write a program which accept N numbers from user and store it into List. Return addition of all
	   prime numbers from that List. Main python file accepts N numbers from user and pass each
	   number to ChkPrime() function which is part of our user defined module named as
	   MarvellousNum. Name of the function from main python file should be ListPrime().

E.g -> Input : Number of elements : 11
       Input Elements : 13 5 45 7 4 56 10 34 2 5 8
       Output : 54 (13 + 5 + 7 +2 + 5)
'''


from MarvellousNum import ChkPrime


def ListPrime(nos):
	sum = 0
	for i in nos:
		sum = sum + i
	return sum


def main():
	Arr = []
	size = int(input("Enter number of elements : "))

	for i in range(size):
		print("Enter the elements : ",i+1)
		no = int(input())
		Arr.append(no)

	print("Entered input is : ",Arr)

	importret = ChkPrime(Arr)

	ret = ListPrime(importret)

	print("Final addition of prime number is : ",ret)


if __name__=="__main__":
	main()
