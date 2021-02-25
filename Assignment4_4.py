'''
Que -> Write a program which contains filter(), map() and reduce() in it. Python application which
	   contains one list of numbers. List contains the numbers which are accepted from user. Filter
	   should filter out all such numbers which are even. Map function will calculate its square.
	   Reduce will return addition of all that numbers.

E.g -> Input List = [5, 2, 3, 4, 3, 4, 1, 2, 8, 10]
   	   List after filter = [2, 4, 4, 2, 8, 10]
	   List after map = [4, 16, 16, 4, 64, 100]
	   Output of reduce = 204
'''

import functools

def main():
	Arr = []
	size = int(input("Enter the number of elements : "))

	for i in range(size):
		print("Enter the elements : ",i+1)
		no = int(input())
		Arr.append(no)

	print("Entered data is : ",Arr)

	f1 = list(filter(lambda no1 : (no1 % 2 == 0),Arr))
	print("Even list after filter : ",f1)

	m1 = list(map(lambda no1 : (no1*no1),f1))
	print("Squared elements after map : ",m1)

	r1 = functools.reduce(lambda no1,no2 : no1 + no2,m1)
	print("Sum output after reduce : ",r1)

if __name__ == "__main__":
	main()