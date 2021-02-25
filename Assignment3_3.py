'''
Que -> Write a program which accept N numbers from user and store it into List. Return Minimum
	   number from that List.

E.g	-> Input : Number of elements : 4
	   Input Elements : 13 5 45 7
	   Output : 5
'''

def FindMin(LIST):
	#return min(LIST)
	min = LIST[0]
	for i in LIST:
		if i < min:
			min = i
	return min		


def main():
	Arr = []
	size = int(input("Enter the number of elements : "))

	for i in range(size):
		print("Enter the element : ",i+1)
		no = int(input())
		Arr.append(no)

	print("Entered input is : ",Arr)	

	ret = FindMin(Arr)

	print("The minimum number in given list is : ",ret)

if __name__=="__main__":
	main()