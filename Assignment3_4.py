'''
Que -> Write a program which accept N numbers from user and store it into List. Accept one another
	   number from user and return frequency of that number from List.

E.g -> Input : Number of elements : 11
	   Input Elements : 13 5 45 7 4 56 5 34 2 5 65
	   Element to search : 5
	   Output : 3
'''

def SearchNo(LIST,nos):
	count = 0
	for i in LIST:		
		if i == nos:
			count = count + 1
	return count		

def main():
	Arr = []
	size = int(input("Enter number of elements : "))

	for i in range(size):
		print("Enter the elements : ",i+1)
		no = int(input())
		Arr.append(no)

	print("Entered input is : ",Arr)

	search = int(input("Enter the number you want to search : "))

	ret = SearchNo(Arr,search)
	print("No. of frequency of given number is : ",ret)

if __name__=="__main__":
	main()