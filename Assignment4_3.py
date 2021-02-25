'''
Que -> Write a program which contains filter(), map() and reduce() in it. Python application which
	   contains one list of numbers. List contains the numbers which are accepted from user. Filter
	   should filter out all such numbers which greater than or equal to 70 and less than or equal to
       90. Map function will increase each number by 10. Reduce will return product of all that
	   numbers.
	   
E.g -> Input List = [4, 34, 36, 76, 68, 24, 89, 23, 86, 90, 45, 70]
   	   List after filter = [76, 89, 86, 90, 70]
	   List after map = [86, 99, 96, 100, 80]
	   Output of reduce = 6538752000
'''

import functools

def main():
	Arr = []
	size = int(input("Enter the number of elements : "))

	for i in range(size):
		print("Enter the element : ",i+1)
		no = int(input())
		Arr.append(no)
	print("Entered data is : ",Arr)

	f1 = list(filter(lambda no1 : (no1>=70 and no1<=90),Arr))
	print("List after filter : ",f1)

	m1 = list(map(lambda no1 : (no1 + 10),f1))
	print("List after map : ",m1)

	r1 = functools.reduce(lambda no1,no2 : (no1*no2),m1)
	print("Output of reduce : ",r1)

if __name__ == "__main__":
	main()